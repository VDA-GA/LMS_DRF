from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'picture', 'course', 'creator']


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture']


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'lesson_count', 'lesson', 'creator']
