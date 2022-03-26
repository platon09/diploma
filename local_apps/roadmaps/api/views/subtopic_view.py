from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from local_apps.roadmaps.models import Subtopic, Topic
from local_apps.roadmaps.api.serializers.subtopic_serializer import SubTopicSerializer


class SubTopicListView(ListAPIView):
    serializer_class = SubTopicSerializer

    def get_queryset(self):
        product_qs = Subtopic.objects.filter(topics__slug=self.kwargs['topic_slug'])
        return product_qs


    def list(self, request, *args, **kwargs):
        topic = Topic.objects.filter(slug=kwargs['topic_slug'],
                                       section__slug=kwargs['section_slug'])
        if not topic:
            raise ValidationError(detail='Topic is not found', code=400)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
