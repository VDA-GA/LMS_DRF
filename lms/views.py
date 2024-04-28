from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from users.permissions import UserIsModerator, IsCreator, UserIsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CourseCreateSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [~UserIsModerator]
        elif self.action in ['destroy', 'update']:
            self.permission_classes = [UserIsNotModerator & IsCreator]
        elif self.action == 'retrieve':
            self.permission_classes = [UserIsModerator | IsCreator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [UserIsNotModerator]

    def perform_create(self, serializer):
        course = serializer.save()
        course.creator = self.request.user
        course.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserIsModerator | IsCreator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsCreator, UserIsNotModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsCreator, UserIsNotModerator]
