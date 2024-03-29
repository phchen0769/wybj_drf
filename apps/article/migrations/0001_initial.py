# Generated by Django 5.0.3 on 2024-03-19 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
