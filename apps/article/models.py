from datetime import datetime
from django.db import models

from apps.user.models import UserProfile


# Create your models here.
class Article(models.Model):
    ranking = models.IntegerField(default=0, verbose_name="排名", help_text="排名")
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="author",
        verbose_name="作者",
        help_text="作者",
    )
    title = models.CharField(null=True,max_length=40, verbose_name="标题", help_text="标题")
    desc = models.CharField(null=True,max_length=100, verbose_name="描述", help_text="描述")
    content = models.CharField(
        null=True,max_length=300, verbose_name="文章内容", help_text="文章内容"
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")

    class Meta:
        app_label = "article"
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title
