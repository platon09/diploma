from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from local_apps.vacancies.models import Vacancy, FavouriteVacancy
from local_apps.vacancies.api.serializers.vacancy_serializer import VacancySerializer

from rest_framework import filters

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class VacancyListView(ListAPIView, UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'employment_type', 'schedule', 'specialization', 'location', 'skill__name']
    ordering_fields = ['created_on', 'salary']

    def update(self, request, *args, **kwargs):
        customer = request.user
        body = request.data
        vacancy_id = body['vacancy_id']
        flag = body['flag']

        if flag:
            query_response = FavouriteVacancy.objects.get_or_create(customer=customer)
            favourite_vacancy = query_response[0]
            is_new_fav_vacancy = query_response[1]
            favourite_vacancies = favourite_vacancy.vacancy.all()
            vacancy = Vacancy.objects.get(id=vacancy_id)

            if vacancy in favourite_vacancies:
                pass


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
