from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=24)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
