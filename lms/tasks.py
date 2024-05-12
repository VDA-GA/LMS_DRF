from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_about_update(email, course_title):
    message = f'Добрый день! Ваш курс {course_title} был обновлен!'
    send_mail(
        subject='Информирование об обновлении курса',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
