from django.db import models
from config.settings import BACKEND_URL
from django.utils.safestring import mark_safe


class Recommendation(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recommendation/images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Recommendations'
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" />')
        except:
            return 'None'

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url
