from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from local_apps.roadmaps.models import Topic, Section
from local_apps.roadmaps.api.serializers.topic_serializer import TopicSerializer


class TopicDetailView(RetrieveAPIView):
    serializer_class = TopicSerializer
    queryset = ''

    def get_object(self):
        topic = Topic.objects.get(slug=self.kwargs['topic_slug'],
                                  section__slug=self.kwargs['section_slug'],
                                  section__specialization__slug=self.kwargs['spec_slug'])
        return topic

    def retrieve(self, request, *args, **kwargs):
        topic = Topic.objects.filter(slug=self.kwargs['topic_slug'],
                                     section__slug=self.kwargs['section_slug'],
                                     section__specialization__slug=self.kwargs['spec_slug'])
        if not topic:
            raise ValidationError(detail='Topic is not found', code=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TopicListView(ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        product_qs = Topic.objects.filter(section__slug=self.kwargs['section_slug'],
                                          section__specialization__slug=self.kwargs['spec_slug'])
        return product_qs


    def list(self, request, *args, **kwargs):
        section = Section.objects.filter(slug=kwargs['section_slug'],
                                         specialization__slug=kwargs['spec_slug'])
        if not section:
            raise ValidationError(detail='Section is not found', code=400)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)