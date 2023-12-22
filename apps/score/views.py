from rest_framework import viewsets
from .models import Answers, Students, Questions, Papers
from .serializers import (
    AnswersSerializer,
    StudentsSerializer,
    QuestionsSerializer,
    PapersSerializer,
)

# 导入simplejwt验证类
from rest_framework_simplejwt.authentication import JWTAuthentication

# 导入drf的过滤器
from django_filters.rest_framework import DjangoFilterBackend

# 导入自定义过滤器
from .filters import StudentsFilter

# 导入drf搜索框
from rest_framework import filters


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    # 需要验证的接口需要设置验证类
    # authentication_classes = (JWTAuthentication,)
    # 过滤器、搜索框
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # 使用自定义过滤类
    filterset_class = StudentsFilter
    # 搜索
    search_fields = ["name", "score"]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
