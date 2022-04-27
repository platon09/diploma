from rest_framework.generics import ListAPIView, RetrieveAPIView

from local_apps.roadmaps.models import Topic, Technology
from local_apps.roadmaps.api.serializers.topic_serializer import TopicDetailSerializer, TopicSerializer


class TopicDetailView(RetrieveAPIView):
    serializer_class = TopicDetailSerializer
    queryset = ''

    def get_object(self):
        topic = Topic.objects.get(id=self.kwargs['topic_id'])
        return topic


class TopicListView(ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topic_qs = Technology.objects.get(id=self.kwargs['tech_id']).topics.all()
        return topic_qs
