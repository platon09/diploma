from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('local_apps.users.urls')),
    path('api/roadmaps/', include('local_apps.roadmaps.urls')),
    path('api/docs/', include_docs_urls(
        title='API documentation'
    )),
]

admin.site.site_header = _("IT Bilim Administration")
admin.site.site_title = _("IT Bilim Admin Portal")
admin.site.index_title = _("Welcome to IT Bilim Portal")
