from rest_framework import serializers
from local_apps.recommendations.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['id', 'title', 'body', 'created_on', 'image_url']