from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Specialization, Section, Topic, Subtopic, MaterialType


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = (('specialization', RelatedOnlyFieldListFilter),)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = (('section', RelatedOnlyFieldListFilter),)


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'link')
    list_filter = (('type', RelatedOnlyFieldListFilter),)


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)