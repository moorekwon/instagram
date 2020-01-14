from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from .models import User
# 장고 기본 유저나 Custom 유저 모델 중, 사용중인 User 모델
from members.forms import LoginForm, SignupForm

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
        # else:
        #     return redirect('members:login')
        #
        #     # form.errors가 살아있는 상태 (form 인스턴스가 유지되고 있음)
        #     # 아래 코드와 중복..
        #     context = {
        #         'form': form
        #     }
        #     return render(request, 'members/login.html', context)
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'members/login.html', context)


def signup_view(request):
    """
    ! config.views.indes 삭제

    Template: index.html을 복사해서
        /members/signup.html
    URL: /
    form: members.forms.SignupForm

    생성에 성공하면, 로그인 처리 후 posts:post-list로 redirect 처리
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post-list')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'members/signup.html', context)

    # email = request.POST['email']
    # username = request.POST['username']
    # name = request.POST['name']
    # password = request.POST['password']
    # # users = User.objects.all()
    # #
    # # if users.filter(username=username) or users.filter(email=email):
    # #     return HttpResponse('이미 사용중인 username/email 입니다.')
    # # else:
    # #     user = User.objects.create_user(email=email, username=username, name=name, password=password)
    # #     login(request, user)
    # #     return redirect('posts:post-list')
    #
    # # 강사님 답안
    # if User.objects.filter(username=username).exists():
    #     return HttpResponse('이미 사용중인 username 입니다.')
    # if User.objects.filter(email=email).exists():
    #     return HttpResponse('이미 사요중인 email 입니다.')
    #
    # user = User.objects.create_user(email=email, username=username, name=name, password=password)
    # login(request, user)
    # return redirect('posts:post-list')


def logout_view(request):
    """
    로그인 되어있는지 확인하고 로그인 되어있을 경우 logout() 시키기.
    """
    logout(request)
    return redirect('members:login')
