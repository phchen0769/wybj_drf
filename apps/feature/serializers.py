from rest_framework import serializers
from .models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Feature
        fields = "id", "title", "percentage", "content", "add_time"
