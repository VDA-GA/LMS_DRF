from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from lms.models import Course, Lesson
from lms.validators import validate_video_link
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[validate_video_link], required=True)

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "picture", "course", "video_link", "creator"]


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "picture"]


class CourseSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    lesson = LessonSerializer(source="lesson_set", many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_subscription(self, course):
        if Subscription.objects.filter(course=course):
            return "подписан"
        else:
            return "не подписан"

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_lesson_count(self, course):
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = ["id", "title", "description", "picture", "lesson_count", "lesson", "creator", "subscription"]
