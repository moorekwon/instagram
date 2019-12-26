from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    """
    Template: templates/members/login.html
    POST 요청을 처리하는 form
    내부에는 input 2개를 가지며, 각각 username, password로 name을 가짐
    URL: /members/login/ (members.urls 사용, config.urls에 include해 사용)
    name: members:login (url namespace 사용)

    POST 요청시, 예제를 보고 적절히 로그인 처리한 후, index로 돌아갈 수 있도록 함
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # return render(request, 'index.html')
            return redirect('index')
        else:
            return redirect('members:login')
            # return render(request, 'members/login.html')
    else:
        return render(request, 'members/login.html')



