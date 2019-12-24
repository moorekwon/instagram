from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostComment


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def comment_create(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST.get('content')

        if not content:
            return HttpResponse('댓글 내용을 입력하세요.', status=400)

        PostComment.objects.create(
            post=post,
            author=request.user,
            content=content
        )

        return redirect('post:post_list')