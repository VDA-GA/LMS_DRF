# Generated by Django 5.0.4 on 2024-04-21 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")),
                (
                    "method",
                    models.CharField(
                        choices=[("перевод на карту", "Card"), ("наличными", "Cash")],
                        max_length=20,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lms.course",
                        verbose_name="оплаченный курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lms.lesson",
                        verbose_name="оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
                "ordering": ("-date",),
            },
        ),
    ]
