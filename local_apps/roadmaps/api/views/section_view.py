from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from local_apps.roadmaps.models import Section, Specialization
from local_apps.roadmaps.api.serializers.section_serializer import SectionSerializer


class SectionListView(ListAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        spec_slug = self.kwargs['spec_slug']
        specialization_qs = Section.objects.filter(specialization__slug=spec_slug)
        return specialization_qs

    def list(self, request, *args, **kwargs):
        spec_slug = self.kwargs['spec_slug']
        specialization = Specialization.objects.filter(slug=spec_slug)
        if not specialization:
            raise ValidationError(detail='Specialization is not found', code=400)

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
