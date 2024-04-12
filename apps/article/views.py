from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Article, Chapter

# # 导入django_filter过滤器
from django_filters.rest_framework import DjangoFilterBackend

# # 导入drf过滤器，主要用于实现模糊搜索以及排序
from rest_framework import filters

from .serializers import ArticleSerializer, ChapterSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # 过滤器、搜索框、排序
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # 排序
    ordering_fields = ["id", "name", "score", "add_time"]


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
