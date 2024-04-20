from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView,
                       LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="create_lesson"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lessons"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
] + router.urls
