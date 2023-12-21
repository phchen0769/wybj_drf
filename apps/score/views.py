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


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    # 需要验证的接口需要设置验证类
    # authentication_classes = (JWTAuthentication,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
