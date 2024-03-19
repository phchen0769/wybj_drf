# Generated by Django 5.0.3 on 2024-03-18 10:01

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField(default=0, help_text='排名', verbose_name='排名')),
                ('title', models.CharField(help_text='标题', max_length=40, null=True, verbose_name='标题')),
                ('desc', models.CharField(help_text='描述', max_length=100, null=True, verbose_name='描述')),
                ('content', models.CharField(help_text='文章内容', max_length=300, null=True, verbose_name='文章内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('author', models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]