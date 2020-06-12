from rest_framework import serializers

from .models import Courses


class GetAllCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields =[
            'id', 'title'
        ]

class CourceSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)
    price = serializers.IntegerField(default=12)