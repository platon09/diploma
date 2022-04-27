from rest_framework import serializers
from local_apps.roadmaps.models import Topic, Subtopic


class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ['name', 'link', 'type']


class TopicDetailSerializer(serializers.ModelSerializer):
    subtopic = serializers.SerializerMethodField()

    def get_subtopic(self, obj):
        out = []
        subtopics = obj.subtopics.all()
        for item in subtopics:
            out.append(SubTopicSerializer(item).data)
        return out

    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'subtopic']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', ]
