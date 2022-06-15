from rest_framework import serializers
from local_apps.roadmaps.models import Technology, UserStudy


class TechnologySerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField(method_name='get_progress')

    def get_progress(self, obj):
        customer = self.context.get('request', None).user
        try:
            progress = UserStudy.objects.get(technology=obj, user=customer).progress
        except:
            progress = 0

        return progress


    class Meta:
        model = Technology
        fields = ['id', 'name', 'description', 'image_url', 'progress']
