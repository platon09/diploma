from django.db import models
from ckeditor.fields import RichTextField
from local_apps.users.models import Skill, Customer


# Class model for determine content type of sub topic
class MaterialType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Material type'
        verbose_name_plural = 'Material types'

    def __str__(self):
        return self.name


# Class model for sub topic of topic
class Subtopic(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    type = models.ForeignKey(MaterialType, related_name='subtopics', on_delete=models.SET_DEFAULT, default='read')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Subtopic'
        verbose_name_plural = 'Subtopics'

    def __str__(self):
        return self.name


# Class model for topic of technology
class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    subtopics = models.ManyToManyField(Subtopic, related_name='topics')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name


# Class model for technology of tech stack
class Technology(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    topics = models.ManyToManyField(Topic, related_name='technologies')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    @property
    def skills(self):
        return ' | '.join(self.skill.all().values_list('name', flat=True))

    def __str__(self):
        return self.name


# Class model for IT specialization
class Specialization(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    technologies = models.ManyToManyField(Technology, related_name='specs')

    class Meta:
        ordering = ('name',)
        verbose_name = 'IT specialization'
        verbose_name_plural = 'IT specializations'

    def __str__(self):
        return self.name


class UserStudy(models.Model):
    technology = models.OneToOneField(Technology, on_delete=models.CASCADE)
    progress = models.FloatField(default=0)
    user = models.ForeignKey(Customer, related_name='userstudies', on_delete=models.CASCADE)
