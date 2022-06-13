from rest_framework import serializers
from local_apps.roadmaps.models import UserStudy


class UserStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStudy
        fields = ('tech_name', 'progress')