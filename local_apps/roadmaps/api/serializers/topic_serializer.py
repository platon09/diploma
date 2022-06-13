from rest_framework import serializers
from local_apps.roadmaps.models import Topic
from local_apps.roadmaps.api.serializers.subtopic_serializer import SubTopicSerializer


class TopicDetailSerializer(serializers.ModelSerializer):
    subtopic = serializers.SerializerMethodField(method_name='get_subtopic')
    is_done = serializers.SerializerMethodField(method_name='checker_for_done')

    def get_subtopic(self, obj):
        return SubTopicSerializer(obj.subtopics.all(), many=True).data

    def checker_for_done(self, obj):
        user = self.context.get('request').user
        is_anonymous = user.is_anonymous

        if is_anonymous:
            return False
        else:
            if obj.user_studies.filter(user=user).count() > 0:
                return True
            else:
                return False

    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'subtopic', 'image_url', 'is_done']


class TopicSerializer(serializers.ModelSerializer):
    is_done = serializers.SerializerMethodField(method_name='checker_for_done')

    def checker_for_done(self, obj):
        user = self.context.get('request').user
        is_anonymous = user.is_anonymous

        if is_anonymous:
            return False
        else:
            if obj.user_studies.filter(user=user).count() > 0:
                return True
            else:
                return False

    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'is_done']
