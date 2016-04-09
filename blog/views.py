from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    today = timezone.now ()
    posts = Post.objects.filter(published_date__lte = today) .order_by("-published_date")
    return render(request, 'blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    today = timezone.now ()
    posts = Post.objects.filter(published_date__lte = today)
    post = posts.get(pk=pk)
    return render(request, 'blog/post_detail.html', {"post": post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form})
