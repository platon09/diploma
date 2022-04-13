from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'image_tag')
