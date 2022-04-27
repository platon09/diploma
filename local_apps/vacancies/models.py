from django.db import models
from ckeditor.fields import RichTextField
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
    employer = models.CharField(max_length=50, blank=True)
    description = RichTextField(blank=True)
    link = models.URLField(blank=True)
    min_salary = models.FloatField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    max_salary = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='vacancies/', null=True, blank=True)
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
    def final_salary(self):
        if self.salary:
            return f"{self.salary} теңге"
        elif self.min_salary and self.max_salary:
            return f"{self.min_salary} теңге - {self.max_salary} теңге аралығы"
        elif self.min_salary:
            return f"{self.min_salary} теңгеден бастап"
        elif self.max_salary:
            return f"{self.max_salary} теңгеге дейін"
        else:
            return "Жалақы көрсетілмеген"

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" style="width: 10%; height: auto;"/>')
        except:
            return 'None'

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url