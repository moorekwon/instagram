from django.shortcuts import render

from .models import Post

app_name = 'posts'


def post_list(request):
    # 1. 로그인 완료 후 이 페이지로 이동
    # 2. index에 접근할 때 로그인이 되어있다면, 이 페이지로 이동
    #     로그인이 되어있는지 확인:
    #         User.is_authenticated가 True인지 체크

    # URL: /posts/ (posts.urls를 사용, config.urls에서 include)
    # Template: templates/posts/post-list.html
    # <h1>Post List</h1>

    # 'posts'라는 키로 모든 Post QuerySet을 전달 (순서는 pk 역순)
    # 전달받은 QuerySet을 순회하며 적절히 Post 내용을 출력

    # posts = Post.objects.all().order_by('-pk')
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }

    return render(request, 'posts/post-list.html', context)
