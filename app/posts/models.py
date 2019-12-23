from django.db import models

from app.config import settings


class Post(models.Model):
    """
    인스타그램의 포스트
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    # PostLike를 통한 Many-to-many 구현
    like_users = models.ManyToManyFielddjango.contrib.auth.models
    created = models.DateTimeField(auto_now_add=True)


class PostImage(models.Model):
    """
    각 포스트의 사진
    """
    post = models.ForeignKey
    image = models.ImageField


class PostComment(models.Model):
    """
    각 포스트의 댓글 (Many-to-one)
    """
    author = models.ForeignKey
    content = models.TextField


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Post 정보를 저장
    Many-to-many 필드를 중간모델(Intermediate Model)을 거쳐 사용
    언제 생성됐는지 extra field로 저장 (created)
    """
    post = models.ForeignKey
    user = models.ForeignKey
    created = models.DateTimeField
