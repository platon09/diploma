from rest_framework.generics import ListAPIView, RetrieveAPIView

from local_apps.roadmaps.models import Topic, Techstack, Technology
from local_apps.roadmaps.api.serializers.topic_serializer import TopicDetailSerializer, TopicSerializer


class TopicDetailView(RetrieveAPIView):
    serializer_class = TopicDetailSerializer
    queryset = ''

    def get_object(self):
        topic = Topic.objects.get(slug=self.kwargs['topic_slug'])
        return topic


class TopicListView(ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topics__ids = Techstack.objects.get(id=self.kwargs['id']).technology.all().prefetch_related('topics').values_list('topics__id', flat=True)
        topic_qs = Topic.objects.filter(technology__slug=self.kwargs['tech_slug'])
        return topic_qs
