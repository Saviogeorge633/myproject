from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title= models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, default='Low')

    def __str__(self):
        return self.title
# Create your models here.
