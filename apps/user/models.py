from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Menu(models.Model):
    """
    菜单
    """

    menu_id = models.IntegerField(
        default=0,
        unique=True,
        primary_key=True,
        verbose_name="菜单ID",
        help_text="菜单ID",
    )
    sub_menu = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="上级菜单",
        help_text="上级菜单",
        related_name="children_menu",
    )
    path = models.CharField(
        default="", max_length=50, verbose_name="路径", help_text="路径"
    )

    component = models.CharField(
        default="", max_length=50, verbose_name="组件名称", help_text="组件名称"
    )
    redirect = models.CharField(
        max_length=30, verbose_name="重定向", help_text="重定向"
    )
    name = models.CharField(max_length=30, verbose_name="路由名", help_text="路由名")
    title = models.CharField(max_length=30, verbose_name="菜单名", help_text="菜单名")
    icon = models.CharField(max_length=50, verbose_name="图标", help_text="图标")

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限
    """

    METHOD_TYPE = (
        (1, "GET"),
        (2, "POST"),
        (3, "DELETE"),
        (4, "PUT"),
        (5, "PATCH"),
        (6, "OPTIONS"),
    )
    # URL别名
    name = models.CharField(
        default="", max_length=30, verbose_name="权限名称", help_text="权限名称"
    )
    method_type = models.IntegerField(
        choices=METHOD_TYPE, verbose_name="方法类型", help_text="方法"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="menu", verbose_name="菜单"
    )

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色
    """

    role_id = models.IntegerField(
        default=0,
        unique=True,
        primary_key=True,
        verbose_name="角色ID",
        help_text="角色ID",
    )

    name = models.CharField(
        default="", max_length=30, verbose_name="角色名称", help_text="角色名称"
    )
    permission = models.ManyToManyField(
        Permission, related_name="role", verbose_name="权限"
    )

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    """
    用户
    """

    username = models.CharField(
        max_length=30, null=True, blank=True, unique=True, verbose_name="姓名"
    )
    avatar = models.CharField(
        max_length=50,
        verbose_name="用户头像",
        help_text="用户头像",
        default="default.jpg",
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

    role = models.ManyToManyField(
        Role,
        # 方便进行反向查询
        related_name="role",
        verbose_name="角色",
    )

    def get_menus(self):
        # 获取该用户所有角色
        roles = self.role.all()
        # 获取所有角色的权限
        permissions = Permission.objects.filter(role__in=roles)
        # 获取所有权限的菜单
        menus = Menu.objects.filter(menu_id__in=permissions)
        return menus

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
