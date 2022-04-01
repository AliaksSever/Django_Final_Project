from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='todos')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug':self.slug})