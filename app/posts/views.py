from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostComment

app_name = 'posts'


def post_list(request):
    # 1. 로그인 완료 후 이 페이지로 이동
    # 2. index에 접근할 때 로그인이 되어있다면, 이 페이지로 이동
    #     로그인이 되어있는지 확인:
    #         User.is_authenticated가 True인지 체크

    # URL: /posts/ (posts.urls를 사용, config.urls에서 include)
    # Template: templates/posts/post-list.html
    # <h1>Post List</h1>
    return render(request, 'posts/post-list.html')














    # posts = Post.objects.all()
    # context = {
    #     'posts': posts
    # }
    #
    # if request.user:
    #     return render(request, 'posts/post-list.html', context)
    # else:
    #     return render(request, 'index.html')
