from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Specialization, Techstack, Technology, Topic, Subtopic, MaterialType


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Techstack)
class TechstackAdmin(admin.ModelAdmin):
    list_display = ('techstack_name', 'specialization')
    list_filter = (('specialization', RelatedOnlyFieldListFilter), ('technology', RelatedOnlyFieldListFilter))


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'skills')
    list_filter = (('skill', RelatedOnlyFieldListFilter),)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology')
    list_filter = (('technology', RelatedOnlyFieldListFilter),)


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = (('type', RelatedOnlyFieldListFilter), ('topics', RelatedOnlyFieldListFilter))

@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)