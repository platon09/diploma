from django.contrib import admin
from .models import Skill, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_login'
    list_display = ('email', 'full_name', 'last_login', 'date_joined', 'is_staff', 'is_active',)
    exclude = ('password', 'groups', 'user_permissions')
    readonly_fields = ('email', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_login',)
    list_filter = ('is_staff', 'is_active',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
