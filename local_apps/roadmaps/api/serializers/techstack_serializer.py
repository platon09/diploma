from rest_framework import serializers
from local_apps.roadmaps.models import Techstack


class TechstackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techstack
        fields = ['id', 'techstack_name', ]
        