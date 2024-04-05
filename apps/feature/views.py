from django.shortcuts import render
from rest_framework import viewsets

from .models import Feature
from .serializers import FeatureSerializer

# Create your views here.


class FeatureViewSet(viewsets.ModelViewSet):
    """
    功能
    """

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
