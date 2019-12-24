from django.urls import path

from . import views
from django.conf.urls import url

from .views import post_list

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list')
]

