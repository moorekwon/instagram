from django.shortcuts import render, redirect


def index(request):
    # base.html 추가
    # 상단에 {% load static %}
    # 정적 파일 불러올 때 {% static '경로' %}로 불러옴

    # index.html과 login.html이 base.html을 extends 하도록 함
    if request.user.is_authenticated:
        return redirect('posts:post-list')
    return render(request, 'index.html')


def asd(request):
    return render(request, 'asd.html')
