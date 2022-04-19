from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'salary', 'image_tag', 'employment_type',
                    'schedule', 'specialization', 'location')
