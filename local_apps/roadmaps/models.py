from django.db import models
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


# Class model for technology of tech stack
class Technology(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200)
    skill = models.ManyToManyField(Skill, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    @property
    def skills(self):
        return ' | '.join(self.skill.all().values_list('name', flat=True))

    def __str__(self):
        return self.name


# Class model for topic of technology
class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    is_learned = models.BooleanField(default=False)
    technology = models.ForeignKey(Technology, related_name='topics',
                                   on_delete=models.SET_DEFAULT, default=None,
                                   null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name


# Class model for sub topic of topic
class Subtopic(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    type = models.ForeignKey(MaterialType, related_name='subtopics', on_delete=models.SET_DEFAULT, default='read')
    topics = models.ManyToManyField(Topic, related_name='topics', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Subtopic'
        verbose_name_plural = 'Subtopics'

    def __str__(self):
        return self.name


# Class model for IT specialization
class Specialization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'IT specialization'
        verbose_name_plural = 'IT specializations'

    def __str__(self):
        return self.name


# Class model for tech stack of IT specialization
class Techstack(models.Model):
    technology = models.ManyToManyField(Technology, related_name='techstacks')
    specialization = models.ForeignKey(Specialization, related_name='techstacks',
                                       on_delete=models.SET_DEFAULT, default=None,
                                       null=True, blank=True)

    class Meta:
        verbose_name = 'Tech stack'
        verbose_name_plural = 'Tech stacks'

    @property
    def techstack_name(self):
        return ' + '.join(self.technology.all().values_list('name', flat=True))

    def __str__(self):
        return ' + '.join(self.technology.all().values_list('name', flat=True))


class UserStudy(models.Model):
    technology = models.OneToOneField(Technology, on_delete=models.CASCADE)
    progress = models.FloatField(default=0)
    user = models.ForeignKey(Customer, related_name='userstudies', on_delete=models.CASCADE)
