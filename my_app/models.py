from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Курс"
        verbose_name_plural: str = "Курсы"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Студент"
        verbose_name_plural: str = "Студенты"



