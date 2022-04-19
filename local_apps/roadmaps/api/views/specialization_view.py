from rest_framework.generics import ListAPIView

from local_apps.roadmaps.models import Specialization
from local_apps.roadmaps.api.serializers.specialization_serializer import SpecializationSerializer


class SpecializationListView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
