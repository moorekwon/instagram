# Generated by Django 2.2.9 on 2020-01-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200115_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.Tag', verbose_name='해시태그 목록'),
        ),
    ]