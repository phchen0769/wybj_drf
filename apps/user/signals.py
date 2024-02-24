# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


# 用于把密码设置为密文形式
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        # 如果密码已经被哈希，那么 `check_password` 方法会返回 `True`
        if not check_password(password, password):
            instance.set_password(password)
            instance.save()
