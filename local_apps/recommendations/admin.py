from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title', 'created_on', 'image_tag')
    list_filter = ('created_on',)
