from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Menu(models.Model):
    """
    菜单
    """

    # MENU_TYPE = (
    #     (1, "一级菜单"),
    #     (2, "二级菜单")
    # )

    name = models.CharField(
        default="", max_length=30, verbose_name="菜单名", help_text="菜单名"
    )
    # menu_type = models.IntegerField(choices=MENU_TYPE, verbose_name="菜单级别", help_text="菜单级别")
    parent_menu = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="父类菜单",
        help_text="父菜单",
        related_name="sub_menu",
    )
    icon = models.CharField(max_length=50, verbose_name="图标")
    # is_menu = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    url_name = models.CharField(default="", max_length=50, verbose_name="图标")

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限
    """

    METHOD_TYPE = ((1, "GET"), (2, "POST"), (3, "DELETE"), (4, "PUT"), (5, "PATCH"))
    # URL别名
    name = models.CharField(
        default="", max_length=30, verbose_name="权限名称", help_text="权限名称"
    )
    method_type = models.IntegerField(
        choices=METHOD_TYPE, verbose_name="方法类型", help_text="方法"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="menu_id", verbose_name="菜单"
    )


class Role(models.Model):
    """
    角色
    """

    ROLE_TYPE = (
        (1, "admin"),
        (2, "teacher"),
        (3, "student"),
    )
    role_type = models.IntegerField(
        choices=ROLE_TYPE, verbose_name="角色", help_text="角色"
    )
    permission = models.ManyToManyField(
        Permission, related_name="permission_id", verbose_name="权限"
    )

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class UserProfile(AbstractUser):
    """
    用户
    """

    username = models.CharField(
        max_length=30, null=True, blank=True, unique=True, verbose_name="姓名"
    )
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    gender = models.CharField(
        max_length=6,
        choices=(("male", "男"), ("female", "女")),
        default="female",
        verbose_name="性别",
    )
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    # role = models.ForeignKey(
    #     Role,
    #     on_delete=models.SET_NULL,
    #     # related_name="role_id",
    #     verbose_name="角色",
    # )

    role = models.ManyToManyField(
        Role,
        related_name="role_id",
        verbose_name="角色",
    )

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class SmsVerifyCode(models.Model):
    """
    短信验证码
    """

    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class EmailVerifyCode(models.Model):
    """
    邮箱验证码
    """

    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.EmailField(unique=True, max_length=100, verbose_name="邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
