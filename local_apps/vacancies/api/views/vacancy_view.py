from rest_framework.generics import ListAPIView, RetrieveAPIView
from local_apps.vacancies.models import Vacancy
from local_apps.vacancies.api.serializers.vacancy_serializer import VacancySerializer

from rest_framework import filters

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response



class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'employment_type', 'schedule', 'specialization', 'location', 'skill__name']
    ordering_fields = ['created_on', 'salary']


class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_object(self):
        vacancy = Vacancy.objects.get(id=self.kwargs['pk'])
        return vacancy

    def retrieve(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.filter(id=self.kwargs['pk'])
        if not vacancy:
            raise ValidationError(detail='Vacancy is not found', code=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
