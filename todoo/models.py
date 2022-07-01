from email.policy import default

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=255)
    created = models.DateField(auto_now_add=True)
    complete = models.DateField(blank=True, auto_now_add=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title