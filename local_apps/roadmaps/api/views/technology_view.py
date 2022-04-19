import json

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from local_apps.roadmaps.models import Techstack, Technology
from local_apps.roadmaps.api.serializers.technology_serializer import TechnologySerializer


class TechnologyListView(ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        technology_qs = Techstack.objects.get(id=pk).technology.all()
        return technology_qs


class RecordProgressView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        is_done = json.loads(request.query_params.get('done'))
        customer = request.user
        tech_skill = Technology.objects.get(slug=kwargs['tech_slug']).skill.all().values_list('id', flat=True)

        if is_done:
            customer.skill.add(*tech_skill)
            return Response(f"Skills added to {request.user.full_name}")
        else:
            customer.skill.remove(*tech_skill)
            return Response(f"Skills removed from {request.user.full_name}")