from rest_framework import serializers
from local_apps.roadmaps.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'slug', 'description']