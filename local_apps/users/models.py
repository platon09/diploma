from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import BACKEND_URL
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Skill(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Customer(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.CharField(max_length=100, blank=True)
    info = models.TextField(blank=True)
    image = models.ImageField(upload_to='customers/', null=True, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Customers'
        ordering = ['-last_login']

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" style="width: 10%; height: auto;"/>')
        except:
            return 'None'

    @property
    def image_url(self):
        try:
            return BACKEND_URL + self.image.url
        except:
            return 'None'
