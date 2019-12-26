from django.contrib import admin

from .models import Post, PostImage, PostComment, PostLike


class PostImageInline(admin.TabularInline):
    pass


class PostCommentInline(admin.TabularInline):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Model
    - Post의 __str__을 적절히 작성

    Admin
    - 작성자, 글, 작성시간이 보여지게 한다
    list_display
    - 상세화면에서 PostImage를 곧바로 추가할 수 있도록 한다
    inlines
    TabularInline (PostImageInline을 적절히 채운 후 사용)
    - PostComment도 곧바로 추가할 수 있도록 한다
    """


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass
