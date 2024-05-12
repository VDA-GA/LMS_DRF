from datetime import datetime, timezone

from celery import shared_task

from users.models import User


@shared_task
def user_blocking():
    today = datetime.now(timezone.utc)
    users = User.objects.filter(is_active=True).exclude(is_superuser=True)
    for user in users:
        if (today - user.last_login).days >= 30:
            user.is_active = False
            user.save()
