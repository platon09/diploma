from rest_framework import serializers
from local_apps.roadmaps.models import Subtopic


class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ['id', 'name', 'link', 'type']