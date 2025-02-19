from django.db import models

from auth_api.models import User


class Room(models.Model):
    """Модель аудитории"""
    room_number = models.CharField(max_length=10)

    class Meta:
        db_table = "rooms"


class Subject(models.Model):
    """Модель предмета"""
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "subjects"


class Exam(models.Model):
    """Модель экзамена"""
    subject_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='exams')

    class Meta:
        db_table = "exams"
