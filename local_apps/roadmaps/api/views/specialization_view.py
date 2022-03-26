from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from local_apps.roadmaps.models import Specialization
from local_apps.roadmaps.api.serializers.specialization_serializer import SpecializationSerializer


class SpecializationListView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SpecializationDetailView(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def get_object(self):
        specialization = Specialization.objects.get(slug=self.kwargs['spec_slug'])
        return specialization

    def retrieve(self, request, *args, **kwargs):
        specialization = Specialization.objects.filter(slug=self.kwargs['spec_slug'])
        if not specialization:
            raise ValidationError(detail='Specialization is not found', code=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
