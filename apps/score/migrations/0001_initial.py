# Generated by Django 5.0.3 on 2024-03-19 09:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('answer', models.CharField(help_text='答案内容', max_length=300, null=True, verbose_name='答案内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '答案',
                'verbose_name_plural': '答案',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(help_text='学生唯一识别号', primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(help_text='学生姓名', max_length=20, null=True, verbose_name='学生姓名')),
                ('score', models.FloatField(default=0, verbose_name='科目得分')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('question_num', models.IntegerField(default=0, help_text='问题唯一识别号', verbose_name='问题num')),
                ('question', models.CharField(help_text='问题内容', max_length=300, null=True, verbose_name='问题内容')),
                ('score', models.FloatField(default=0, verbose_name='分数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.answers')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题目',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(help_text='试卷唯一识别号', primary_key=True, serialize=False, verbose_name='试卷id')),
                ('title', models.CharField(help_text='试卷标题', max_length=300, null=True, verbose_name='试卷标题')),
                ('score', models.FloatField(default=0, verbose_name='试卷总分')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('question', models.ManyToManyField(to='score.questions')),
                ('student', models.ManyToManyField(to='score.students')),
            ],
            options={
                'verbose_name': '试卷',
                'verbose_name_plural': '试卷',
            },
        ),
    ]
