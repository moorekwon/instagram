# Generated by Django 2.2.9 on 2020-01-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_content_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='posts.Tag', verbose_name='해시태그 목록'),
        ),
    ]