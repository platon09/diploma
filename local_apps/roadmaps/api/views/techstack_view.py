from rest_framework.generics import ListAPIView

from local_apps.roadmaps.models import Techstack
from local_apps.roadmaps.api.serializers.techstack_serializer import TechstackSerializer


class TechstackListView(ListAPIView):
    serializer_class = TechstackSerializer

    def get_queryset(self):
        techstack_qs = Techstack.objects.filter(specialization__slug=self.kwargs['spec_slug'])
        return techstack_qs
