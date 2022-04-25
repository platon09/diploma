from rest_framework.generics import ListAPIView

from local_apps.roadmaps.models import Specialization
from local_apps.roadmaps.api.serializers.techstack_serializer import TechstackSerializer


class TechstackListView(ListAPIView):
    serializer_class = TechstackSerializer

    def get_queryset(self):
        techstack_qs = Specialization.objects.get(id=self.kwargs('id')).techstacks.all()
        return techstack_qs
