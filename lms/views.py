from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson
from lms.paginators import CustomPagination
from lms.serializers import CourseCreateSerializer, CourseSerializer, LessonSerializer
from users.permissions import IsCreator, UserIsModerator, UserIsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.user.groups.filter(name="Moderators").exists():
            queryset = Course.objects.all()
        else:
            queryset = Course.objects.filter(creator=self.request.user)
        return queryset

    def perform_create(self, serializer):
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~UserIsModerator]
        elif self.action == "destroy":
            self.permission_classes = [UserIsNotModerator & IsCreator]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [UserIsModerator | IsCreator]
        elif self.action == "list":
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
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.user.groups.filter(name="Moderators").exists():
            queryset = Lesson.objects.all()
        else:
            queryset = Lesson.objects.filter(creator=self.request.user)
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [UserIsModerator | IsCreator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsCreator | UserIsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsCreator, UserIsNotModerator]
