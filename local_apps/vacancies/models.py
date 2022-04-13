from django.db import models
from local_apps.users.models import Skill
from config.settings import BACKEND_URL
from django.utils.safestring import mark_safe


class Vacancy(models.Model):
    EMPLOYMENT_TYPE_CHOICES = (
        ("FULL_TIME", "Full time"),
        ("PART_TIME", "Part time"),
        ("INTERNSHIP", "Internship"),
        ("PROJECT_WORK", "Project work"),
        ("VOLUNTEERING", "Volunteering"),
    )
    SCHEDULE_CHOICES = (
        ("FULL_DAY", "Full day"),
        ("SHIFT_WORK", "Shift work"),
        ("SHIFT_METHOD", "Shift method"),
        ("REMOTE_WORK", "Remote work"),
        ("FLEXIBLE", "Flexible"),
    )
    SPEC_CHOICES = (
        ("BACK_END", "Back-end"),
        ("FRONT_END", "Front-end"),
        ("ANDROID", "Android"),
        ("IOS", "iOS"),
        ("DEVOPS", "DevOps"),
        ("NETWORK_ENGINEERING", "Network Engineering"),
        ("DATA_ENGINEERING", "Data Engineering"),
        ("ML/AI", "ML/AI"),
        ("DATA_SCIENCE", "Data Science"),
        ("DESKTOP_DEV", "Desktop app development")
    )
    title = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    salary = models.FloatField()
    image = models.ImageField(upload_to='vacancies/images/', null=True, blank=True)
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE_CHOICES, default="INTERNSHIP")
    schedule = models.CharField(max_length=15, choices=SCHEDULE_CHOICES, default="FULL_DAY")
    specialization = models.CharField(max_length=20, choices=SPEC_CHOICES, default="BACK_END")
    location = models.CharField(max_length=140)
    skill = models.ManyToManyField(Skill, blank=True)

    class Meta:
        verbose_name_plural = 'Vacancy'
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
        if self.image:
            return BACKEND_URL + self.image.url
        else:
            'None'
