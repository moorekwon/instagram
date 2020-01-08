from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import PostCreateForm, CommentCreateForm
from .models import Post, PostLike, PostImage, PostComment

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
    comment_form = CommentCreateForm()

    context = {
        'posts': posts,
        'comment_form': comment_form
    }

    return render(request, 'posts/post-list.html', context)


def post_like(request, pk):
    """
    pk가 pk인 Post와 (변수명 post 사용)
    request.user로 전달되는 User(변수명 user 사용)에 대해

    1. PostLike(post=post, user=user)인 PostLike 객체가 존재하는지 확인
    2-1. 만약 해당 객체가 이미 있다면, 삭제
    2-2. 만약 해당 객체가 없다면, 새로 생성
    3. 완료 후, posts:post-list로 redirect
    """
    # pk로 Post 가져오기
    # Post.objects.get(키=값)

    # PostLike 객체가 있는지 검사
    # 검색: Django queryset exists
    # PostLike.objects.filter(키1=값1, 키2=값2).exists()

    # 삭제
    # PostLike.objects.filter(조건).delete()

    # redirect
    # return redirect(URL name)

    post = Post.objects.get(pk=pk)
    user = request.user

    post_like_qs = PostLike.objects.filter(post=post, user=user)
    # user, post에 해당하는 PostLike가 있는 경우
    if post_like_qs.exists():
        # 삭제
        post_like_qs.delete()
    # 없는 경우
    else:
        # 생성
        PostLike.objects.create(post=post, user=user)
    return redirect('posts:post-list')


def post_create(request):
    """
    URL: /posts/create/, name='post-create'
    Template: /posts/post-create.html

    forms.PostCreateForm 사용
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 새 Post 생성
        # user는 request.user
        # 전달받는 데이터: image, text
        user = request.user
        # image = request.FILES['image']
        text = request.POST['text']

        # Post 생성 (변수명 post 사용)
        # request.user와 text 사용
        post = Post.objects.create(author=user, content=text)

        # PostImage 생성
        # post와 전달받은 image 사용
        # post_image = PostImage.objects.create(post=post, image=image)

        images = request.FILES.getlist('image')

        for image in images:
            PostImage.objects.create(post=post, image=image)

        # 모든 생성이 완료되면 posts:post-list로 redirect
        return redirect('posts:post-list')
    else:
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'posts/post-create.html', context)


def comment_create(request, post_pk):
    # URL: /posts/<int:post_pk>/comments/create/
    # Template: 없음 (post-list.html에 Form 구현)
    # post-list.html 내부에서, 각 Post마다 자신에게 연결된 PostComment 목록을 보여줌

    # 보여주는 형식
    # <ul>
    #   <li><b>작성자명</b><span>내용</span></li>
    #   <li><b>작성자명</b><span>내용</span></li>
    # </ul>

    # Form: post.forms.CommentCreateForm

    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            form.save(post=post, author=request.user)
        return redirect('posts:post-list')

