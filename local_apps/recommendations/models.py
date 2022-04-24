from django.db import models
from config.settings import BACKEND_URL


class Image(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return BACKEND_URL+self.photo.url


class Recommendation(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        verbose_name_plural = 'Recommendations'
        ordering = ['-created_on']

    def __str__(self):
        return self.title
