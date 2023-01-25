

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
