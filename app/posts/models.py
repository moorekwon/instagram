import re

from django.db import models

from members.models import User


class Post(models.Model):
    TAG_PATTERN = re.compile(r'#(\w+)')
    """
    인스타그램의 포스트
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    content_html = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', verbose_name='해시태그 목록', related_name='posts', blank=True)

    # PostLike를 통한 Many-to-many 구현
    like_users = models.ManyToManyField(
        User,
        through='PostLike',
        related_name='like_post_set'
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{author} | {created}'.format(
            author=self.author.username,
            created=self.created
        )

    def _save_html(self):
        """
        content 속성의 값을 사용해 해시태그에 해당하는 문자열을 a 태그로 바꿔줌
        """
        self.content_html = re.sub(
            self.TAG_PATTERN,
            r'<a href="/explore/tags/\g<1>/">#\g<1></a>',
            self.content
        )

    def _save_tags(self):
        """
        content에 포함된 해시태그 문자열(예: #Python)의 Tag들을 만듦
        자신의 tags Many-to-many field에 추가
        """
        # instagram, created = Tag.objects.get_or_create(속성)
        # ManyToManyField.set 사용
        tag_name_list = re.findall(self.TAG_PATTERN, self.content)
        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_name_list]
        self.tags.set(tags)

        # for tag_name in tag_name_list:
        #     tag = Tag.objects.get_or_create(name=tag_name)[0]
        #     self.tags.add(tag)

    def save(self, *args, **kwargs):
        """
        Post 객체가 저장될 때, content 값을 분석해서
        자신의 tags 항목을 적절히 채워줌

        ex) #Django #Python이 온 경우,
        post.tags.all() 시, name이 Django, Python인 Tag 2개 QuerySet이 리턴
        """
        self._save_html()
        super().save(*args, **kwargs)
        self._save_tags()
        # self.tags.clear()


class PostImage(models.Model):
    """
    각 포스트의 사진
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images')


class PostComment(models.Model):
    """
    각 포스트의 댓글 (Many-to-one)

    postcomment_set <- related_name
    반대쪽 객체에서 사용
    post.postcomment_set

    postcomment <- related_query_name
    반대쪽 QuerySet의 filter 조건 키워드명으로 사용
    Post.objects.filter(postcomment__)

    기본값
    related_name: <모델클래스명의 lowercase>_set
    related_query_name: <모델클래스명의 lowercase>
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Post 정보를 저장
    Many-to-many 필드를 중간모델(Intermediate Model)을 거쳐 사용
    언제 생성됐는지 extra field로 저장 (created)
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    """
    Many-to-many에서 필드는 Post에 클래스에 작성
    HashTag의 Tag를 담당
    Post 입장에서 post.tags.all()로 연결된 전체 Tag를 불러올 수 있어야 함
    Tag 입장에서 tag.posts.all()로 연결된 전체 Post를 불러올 수 있어야 함

    Django admin에서 결과를 볼 수 있도록 amdin.py에 적절히 내용 기록

    중개모델(Intermediate model) 사용할 필요 없음
    """
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name
