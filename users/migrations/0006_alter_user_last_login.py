# Generated by Django 4.2.1 on 2024-05-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_payment_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(auto_now=True, null=True, verbose_name="Дата последнего входа"),
        ),
    ]
