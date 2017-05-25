from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.content
