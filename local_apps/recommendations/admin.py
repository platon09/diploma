from django.contrib import admin
from .models import Recommendation, Image


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on')
    list_filter = ('created_on',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image_tag_for_list')
    readonly_fields = ('image_url', 'image_tag_for_detail')