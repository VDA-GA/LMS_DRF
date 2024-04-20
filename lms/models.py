from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(**NULLABLE, verbose_name="Описание курса")
    picture = models.ImageField(upload_to="lms/", **NULLABLE, verbose_name="Превью")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(**NULLABLE, verbose_name="Описание курса")
    picture = models.ImageField(upload_to="lms/", **NULLABLE, verbose_name="Превью")
    video_link = models.CharField(max_length=300, **NULLABLE, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
