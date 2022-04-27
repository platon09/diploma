from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Specialization, Technology, Topic, Subtopic, MaterialType, UserStudy


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    pass


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStudy)
class UserStudyAdmin(admin.ModelAdmin):
    pass