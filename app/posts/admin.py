from django.contrib import admin

from .models import Post, PostImage, PostComment, PostLike


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 1


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
    list_display = ('author', 'content', 'created')
    list_display_links = ('author', 'content')

    inlines = [
        PostImageInline,
        PostCommentInline
    ]



@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass
