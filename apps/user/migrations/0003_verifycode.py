# Generated by Django 5.0 on 2023-12-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_emailverifycode_rename_verifycode_smsverifycode'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='邮箱')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '验证码',
                'verbose_name_plural': '验证码',
            },
        ),
    ]
