from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_payment = [
            {
                "user": User.objects.get(email="test1@mail.ru"),
                "date": "2024-03-17",
                "course": Course.objects.get(pk=3),
                "method": "перевод на карту",
            },
            {
                "user": User.objects.get(email="test1@mail.ru"),
                "date": "2022-03-20",
                "lesson": Lesson.objects.get(pk=1),
                "method": "перевод на карту",
            },
            {
                "user": User.objects.get(email="test1@mail.ru"),
                "date": "2023-03-21",
                "lesson": Lesson.objects.get(pk=2),
                "method": "перевод на карту",
            },
            {
                "user": User.objects.get(email="test2@mail.ru"),
                "date": "2020-04-17",
                "course": Course.objects.get(pk=3),
                "method": "перевод на карту",
            },
            {
                "user": User.objects.get(email="test2@mail.ru"),
                "date": "2021-12-22",
                "lesson": Lesson.objects.get(pk=1),
                "method": "наличными",
            },
            {
                "user": User.objects.get(email="test2@mail.ru"),
                "date": "2020-10-19",
                "course": Course.objects.get(pk=3),
                "method": "наличными",
            },
            {
                "user": User.objects.get(email="test3@mail.ru"),
                "date": "2024-04-10",
                "lesson": Lesson.objects.get(pk=2),
                "method": "перевод на карту",
            },
            {
                "user": User.objects.get(email="test3@mail.ru"),
                "date": "2024-04-11",
                "lesson": Lesson.objects.get(pk=3),
                "method": "наличными",
            },
        ]

        for payment_item in list_payment:
            Payment.objects.create(**payment_item)
