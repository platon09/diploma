from rest_framework import serializers
from local_apps.roadmaps.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'slug']