from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20)
