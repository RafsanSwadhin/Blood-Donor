from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .forms import PostForm
from .models import Post
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Post creation view
@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associate the post with the current user
            post.slug = slugify(post.title)  # Generate the slug
            post.save()
            return redirect('postview')  # Update to your URL name
    else:
        form = PostForm()
    return render(request, 'createpost.html', {'form': form})


# Post view with pagination
def postview(request):
    post = Post.objects.all().order_by('-created_at')  # Order by latest posts
    paginator = Paginator(post, 12)  # Show 12 posts per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameter
    page_obj = paginator.get_page(page_number)  # Get the corresponding page
    context = {
        'post': page_obj,
        'post_model': Post,  # Passing the model to access CITY and GROUP choices
    }
    return render(request, 'postview.html', context)


# Post detail view
# @login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# Filtered post view
def filtered_post_view(request):
    city = request.GET.get('city', None)
    group = request.GET.get('group', None)
    page_number = request.GET.get('page', 1)  # Get the current page number

    # Check if at least one field is filled
    if not city and not group:
        messages.error(request, "Please select at least one filter: City or Blood Group.")
        return render(request, 'filtered_posts.html', {'posts': []})

    # Filter posts based on city and blood group
    posts = Post.objects.all()
    if city:
        posts = posts.filter(city=city)
    if group:
        posts = posts.filter(group__icontains=group)

    # Paginate the posts (10 posts per page)
    paginator = Paginator(posts, 10)
    paginated_posts = paginator.get_page(page_number)

    return render(request, 'filtered_posts.html', {'posts': paginated_posts})


# Post edit view
@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Ensure the post has a user associated with it
    if post.user != request.user:  # Make sure the post belongs to the current user
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form, 'post': post})


# Post delete view
@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:  # Make sure the post belongs to the current user
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == 'POST':
        post.delete()
        return redirect('filtered_post_view')  # Redirect to a suitable page after deletion
    return render(request, 'post_confirm_delete.html', {'post': post})


# Registration view
def registration_view(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in immediately
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('/')  # Redirect to homepage or any other page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})
