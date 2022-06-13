from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.utils.html import format_html
from config.settings import BACKEND_URL

from django.contrib.admin.models import LogEntry
from .models import Skill, Customer


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'
    exclude = ['object_repr', 'change_message']
    readonly_fields = ('action_time', 'user', 'action_flag', 'object_id', '__str__',
                       'link', 'content_type',)
    ordering = ('-action_time',)
    search_fields = ('content_type', '__str__', 'user')
    list_display = ('action_time', 'user', 'action_flag', '__str__', 'link',)
    list_filter = ('action_flag', ('user', RelatedOnlyFieldListFilter),
                   ('content_type', RelatedOnlyFieldListFilter))

    def get_queryset(self, request):
        queryset = super(LogEntryAdmin, self).get_queryset(request)
        if request.resolver_match.func.__name__ not in ['change_view', 'add_view']:
            qs = queryset.select_related('content_type', 'user')
        else:
            qs = queryset
        return qs

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    @staticmethod
    def link(obj):
        admin_url = obj.get_admin_url()
        if admin_url:
            url = BACKEND_URL + admin_url
            return format_html('<a href="{}">{}</a>', url, 'link to '+obj.object_repr)
        return "null"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_login'
    list_display = ('id', 'email', 'full_name', 'last_login', 'date_joined', 'is_staff', 'is_active',)
    exclude = ('password', 'groups', 'user_permissions')
    readonly_fields = ('email', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_login',)
    list_filter = ('is_staff', 'is_active',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
