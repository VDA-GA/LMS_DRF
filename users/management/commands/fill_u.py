from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_users = [
            {"email": "test1@mail.ru"},
            {"email": "test2@mail.ru"},
            {"email": "test3@mail.ru"},
        ]

        for user_item in list_users:
            User.objects.create(**user_item)
