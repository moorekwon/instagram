from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from .models import User
# 장고 기본 유저나 Custom 유저 모델 중, 사용중인 User 모델
from members.forms import LoginForm

User = get_user_model()


def login_view(request):
    """
    Template: templates/members/login.html
    POST 요청을 처리하는 form
    내부에는 input 2개를 가지며, 각각 username, password로 name을 가짐
    URL: /members/login/ (members.urls 사용, config.urls에 include해 사용)
    name: members:login (url namespace 사용)

    POST 요청시, 예제를 보고 적절히 로그인 처리한 후, index로 돌아갈 수 있도록 함
    """
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)
    #         # return render(request, 'index.html')
    #         # return redirect('index')
    #         return redirect('posts:post-list')
    #     else:
    #         return redirect('members:login')
    #         # return render(request, 'members/login.html')
    # else:
    #     return render(request, 'members/login.html')

    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)

        form = LoginForm(request.POST)

        if form.is_valid():
            # user = authenticate(request)
            # if user:
            #     login(request, user)
            #     return redirect('posts:post-list')
            # else:
            #     return redirect('members:login')

            form.login(request)
            return redirect('posts:post-list')
        # 아이디 혹은 비밀번호가 잘못되면 members:login 페이지로 다시 load
        else:
            return redirect('members:login')

    form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'members/login.html', context)


def signup_view(request):
    """
    Template: index.html을 그대로 사용
        action만 이쪽으로
    URL: /members/signup/
    User에 name필드를 추가
        email
        username
        name
        password
    를 전달받아, 새로운 User를 생성한다
    생성시, User.objects.create_user() 메서드를 사용한다
    이미 존재하는 username또는 email을 입력한 경우,
    "이미 사용중인 username/email입니다" 라는 메시지를 HttpResponse로 돌려준다
    생성에 성공하면 로그인 처리 후 (위의 login_view를 참조) posts:post-list로 redirect처리
    :param request:
    :return:
    """
    email = request.POST['email']
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']
    # users = User.objects.all()
    #
    # if users.filter(username=username) or users.filter(email=email):
    #     return HttpResponse('이미 사용중인 username/email 입니다.')
    # else:
    #     user = User.objects.create_user(email=email, username=username, name=name, password=password)
    #     login(request, user)
    #     return redirect('posts:post-list')

    # 강사님 답안
    if User.objects.filter(username=username).exists():
        return HttpResponse('이미 사용중인 username 입니다.')
    if User.objects.filter(email=email).exists():
        return HttpResponse('이미 사요중인 email 입니다.')

    user = User.objects.create_user(email=email, username=username, name=name, password=password)
    login(request, user)
    return redirect('posts:post-list')


def logout_view(request):
    """
    로그인 되어있는지 확인하고 로그인 되어있을 경우 logout() 시키기.
    """
    logout(request)
    return redirect('members:login')
