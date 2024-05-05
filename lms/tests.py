from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testor@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Course-1", creator=self.user)
        self.lesson = Lesson.objects.create(
            name="Lesson-1", course=self.course, video_link="https://www.youtube.com/watch/1", creator=self.user
        )

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("lms:create_lesson")
        data = {"name": "Lesson-2", "course": self.course.pk, "video_link": "https://www.youtube.com/watch/2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Lesson-NEW", "course": self.course.pk, "video_link": "https://www.youtube.com/watch/666"}
        response = self.client.put(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("name"), "Lesson-NEW")
        self.assertEqual(result.get("video_link"), "https://www.youtube.com/watch/666")

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lessons")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "picture": self.lesson.picture,
                    "course": self.course.pk,
                    "video_link": self.lesson.video_link,
                    "creator": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def tearDown(self):
        pass


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testor@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Course-1", creator=self.user)
        self.url = reverse("users:subscription")
        self.data = {"id": self.course.pk}

    def test_post(self):
        response = self.client.post(self.url, self.data)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("message"), "подписка добавлена")
