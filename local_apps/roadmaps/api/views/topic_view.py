from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from local_apps.roadmaps.models import Topic, Technology, UserStudy
from local_apps.roadmaps.api.serializers.topic_serializer import TopicDetailSerializer, TopicSerializer

from rest_framework.response import Response


class TopicDetailView(RetrieveAPIView):
    serializer_class = TopicDetailSerializer
    queryset = ''

    def get_object(self):
        topic = Topic.objects.get(id=self.kwargs['topic_id'])
        return topic


class TopicListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer

    def get_queryset(self):
        tech = Technology.objects.get(id=self.kwargs['tech_id'])
        topic_qs = tech.topics.all()

        customer = self.request.user
        try:
            progress = UserStudy.objects.get(technology=tech, user=customer).progress
        except:
            progress = 0

        tech_progress_data = {
            "tech": tech.name,
            "progress": progress
        }

        return topic_qs, tech_progress_data

    def list(self, request, *args, **kwargs):
        qs, progress = self.get_queryset()

        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            "tech_data": progress,
            "data": serializer.data
        }

        return Response(response_data)
