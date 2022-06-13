from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Specialization, Technology, Topic, Subtopic, MaterialType, UserStudy


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_techs')
    list_filter = ('name', ('technologies', RelatedOnlyFieldListFilter))


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_topics', 'image_url')
    list_filter = ('name', ('topics', RelatedOnlyFieldListFilter),)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_subtopics', 'num_skills', 'image_url')
    list_filter = ('name', ('subtopics', RelatedOnlyFieldListFilter), ('skills', RelatedOnlyFieldListFilter),)


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'type',)
    list_filter = ('link', ('type', RelatedOnlyFieldListFilter),)


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(UserStudy)
class UserStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'technology', 'user', 'progress',)
    list_filter = ('technology', 'user', 'progress', ('topics', RelatedOnlyFieldListFilter))