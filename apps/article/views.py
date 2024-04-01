from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Article, Chapter

from .serializers import ArticleSerializer, ChapterSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = []


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = []
