import uuid

from django.db import models

from common.models import TimestampModel


class School(TimestampModel):
    name = models.CharField(max_length=255)
    student_max_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(TimestampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    identification = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True, related_name='students')

    def __str__(self):
        return self.first_name
