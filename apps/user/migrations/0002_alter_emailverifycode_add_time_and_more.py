# Generated by Django 5.0.3 on 2024-03-18 09:25

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='emailverifycode',
            name='code',
            field=models.CharField(help_text='验证码', max_length=10, null=True, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='emailverifycode',
            name='email',
            field=models.EmailField(help_text='邮箱', max_length=100, null=True, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='sub_menu',
            field=models.ForeignKey(blank=True, help_text='上级菜单', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='user.menu', verbose_name='上级菜单'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(help_text='菜单', on_delete=django.db.models.deletion.CASCADE, related_name='permission', to='user.menu', verbose_name='菜单'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(help_text='权限', related_name='permission', to='user.permission', verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='smsverifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='smsverifycode',
            name='code',
            field=models.CharField(help_text='验证码', max_length=10, null=True, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='smsverifycode',
            name='mobile',
            field=models.CharField(help_text='手机', max_length=11, null=True, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, help_text='生日', null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, help_text='邮箱', max_length=100, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', help_text='性别', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(help_text='手机', max_length=11, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(help_text='角色', related_name='role', to='user.role', verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, help_text='姓名', max_length=30, null=True, unique=True, verbose_name='姓名'),
        ),
    ]