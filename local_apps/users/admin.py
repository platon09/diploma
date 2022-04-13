from django.contrib import admin
from .models import Customer, Skill


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_login'
    list_display = ('email', 'full_name', 'last_login', 'is_staff', 'is_active',)
    readonly_fields = ('password', 'email', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_login',)
    list_filter = ('is_staff', 'is_active',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)