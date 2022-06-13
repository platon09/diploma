from rest_framework import serializers
from local_apps.roadmaps.models import Topic, Subtopic


class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ['name', 'link', 'type_name']


class TopicDetailSerializer(serializers.ModelSerializer):
    subtopic = serializers.SerializerMethodField(method_name='get_subtopic')
    is_done = serializers.SerializerMethodField(method_name='checker_for_done')

    def get_subtopic(self, obj):
        out = []
        subtopics = obj.subtopics.all()
        for item in subtopics:
            out.append(SubTopicSerializer(item).data)
        return out

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
