from django.db import models


# Class model for IT specialization
class Specialization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'IT specialization'
        verbose_name_plural = 'IT specializations'

    def __str__(self):
        return self.name


# Class model for section of IT specialization
class Section(models.Model):
    specialization = models.ManyToManyField(Specialization, related_name='sections')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'section'
        verbose_name_plural = 'sections'

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'material type'
        verbose_name_plural = 'material types'

    def __str__(self):
        return self.name


# Class model for subtopic of topic
class Subtopic(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    type = models.ForeignKey(MaterialType, related_name='subtopics', on_delete=models.SET_DEFAULT, default='read')

    class Meta:
        ordering = ('name',)
        verbose_name = 'subtopic'
        verbose_name_plural = 'subtopics'

    def __str__(self):
        return self.name


# Class model for topic of section
class Topic(models.Model):
    section = models.ManyToManyField(Section, related_name='topics')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    is_learned = models.BooleanField(default=False)
    subtopic = models.ManyToManyField(Subtopic, related_name='topics')

    class Meta:
        ordering = ('name',)
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.name
