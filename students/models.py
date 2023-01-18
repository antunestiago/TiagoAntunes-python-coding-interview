from django.db import models
from subjects.models import Subject


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)
    subjects = models.ManyToManyField(Subject)
    enrollment = models.BooleanField()

    def __str__(self):
        return self.name
