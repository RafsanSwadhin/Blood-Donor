
from django.shortcuts import render, redirect ,get_object_or_404
from django.utils.text import slugify
from .forms import PostForm
from .models import Post

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




def postview(request):
    post = Post.objects.all().order_by('-created_at')  # Order by latest posts
    return render(request, 'postview.html', {'post': post})


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})