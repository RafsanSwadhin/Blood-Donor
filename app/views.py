from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'basic.html')

from django.shortcuts import render, redirect
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
            return redirect('/')  # Update to your URL name
    else:
        form = PostForm()
    return render(request, 'createpost.html', {'form': form})
