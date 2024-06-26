from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="номер телефона")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="аватарка")
    city = models.CharField(max_length=100, **NULLABLE, verbose_name="город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    class Method(models.TextChoices):
        CARD = "перевод на карту"
        CASH = "наличными"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="оплаченный курс")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name="оплаченный урок")
    method = models.CharField(max_length=20, choices=Method.choices, verbose_name="способ оплаты")
    session_id = models.CharField(max_length=250, **NULLABLE, verbose_name="id сессии")
    payment_link = models.URLField(max_length=500, **NULLABLE, verbose_name="Ссылка на оплату")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сумма")

    def __str__(self):
        return f"{self.user} - {self.course if self.course else self.lesson}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ("-date",)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
