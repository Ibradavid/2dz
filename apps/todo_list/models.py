from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовк задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описание для задачи")
    completed = models.BooleanField(default=False, verbose_name="Статус выполнения")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания задачи")

    def __str__(self):
        return self.title
