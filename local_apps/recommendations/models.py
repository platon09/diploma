from django.db import models
from ckeditor.fields import RichTextField
from config.settings import BACKEND_URL
from django.utils.safestring import mark_safe


class Image(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return BACKEND_URL + self.photo.url

    @property
    def image_tag_for_list(self):
        try:
            return mark_safe(f'<img src="{self.photo.url}" style="width: 10%; height: auto;"/>')
        except:
            return 'None'

    @property
    def image_tag_for_detail(self):
        try:
            return mark_safe(f'<img src="{self.photo.url}" style="width: 50%; height: auto;"/>')
        except:
            return 'None'

    @property
    def image_url(self):
        try:
            return BACKEND_URL + self.photo.url
        except:
            return None


class Recommendation(models.Model):
    title = models.CharField(max_length=140)
    body = RichTextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        verbose_name_plural = 'Recommendations'
        ordering = ['-created_on']

    def __str__(self):
        return self.title
