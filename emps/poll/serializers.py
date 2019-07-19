from django.contrib.auth.models import User
from rest_framework import serializers

from poll.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'title',
            'status',
            'created_by',
        ]


# class QuestionS(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=256)
#     status = serializers.CharField(max_length=10, default='inactive')
#     created_by = serializers.PrimaryKeyRelatedField()
#     start_date = serializers.DateTimeField(null=True, blank=True)
#     end_date = serializers.DateTimeField(null=True, blank=True)
#     created_at = serializers.DateTimeField(auto_now_add=True)
#     updated_at = serializers.DateTimeField(auto_now=True)
