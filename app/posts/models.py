from django.db import models


class Post(models.Model):
    """
    인스타그램의 포스트
    """
    author =
    content =
    like_users = 'PostLike를 통한 Many-to-many 구현'
    created =
    pass


class PostImage(models.Model):
    """
    각 포스트의 사진
    """
    pass


class PostComment(models.Model):
    """
    각 포스트의 댓글 (Many-to-one)
    """
    pass


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Post 정보를 저장
    Many-to-many 필드를 중간모델(Intermediate Model)을 거쳐 사용
    언제 생성됐는지 extra field로 저장 (created)
    """
    pass
