import json

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from local_apps.roadmaps.models import Specialization, UserStudy, Technology, Topic
from local_apps.roadmaps.api.serializers.technology_serializer import TechnologySerializer


class TechnologyListView(ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        pk = self.kwargs['spec_id']
        technology_qs = Specialization.objects.get(id=pk).technologies.all()
        return technology_qs


class RecordProgressView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        is_done = json.loads(request.query_params.get('done'))
        customer = request.user
        tech_id = kwargs['tech_id']
        topic_id = kwargs['topic_id']

        tech = Technology.objects.get(id=tech_id)
        topic = Topic.objects.get(id=topic_id)

        response = UserStudy.objects.userstudy_progress(tech, topic, customer, is_done)
        return response
