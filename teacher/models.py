from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='courses/')
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    detailes = models.CharField(max_length=500)
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    
    due_date = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title