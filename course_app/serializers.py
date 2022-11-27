from rest_framework import serializers
from course_app.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'photo', 'time_study']


class CourseDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
