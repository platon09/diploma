from rest_framework import serializers
from local_apps.recommendations.models import Image, Recommendation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_url',)


class RecommendationSerializer(serializers.ModelSerializer):
    pics = serializers.SerializerMethodField('get_images')

    def get_images(self, obj):
        out = []
        images = obj.images.all()
        for item in images:
            out.append(ImageSerializer(item).data)
        return out

    class Meta:
        model = Recommendation
        fields = ['id', 'title', 'body', 'created_on', 'pics']