import json

from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from local_apps.vacancies.models import Vacancy, FavouriteVacancy
from local_apps.vacancies.api.serializers.vacancy_serializer import VacancySerializer

from rest_framework import filters

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class VacancyListView(ListAPIView, UpdateAPIView):
    serializer_class = VacancySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'employment_type', 'schedule', 'specialization', 'location', 'skill__name']
    ordering_fields = ['created_on', 'salary']

    def get_queryset(self):
        recommend = json.loads(self.request.query_params.get('recommend', 'false'))
        #TODO надо закончить умный список вакансии
        if recommend:
            needed_skills = self.request.user.skill.all()
            return Vacancy.objects.filter(skill__in=needed_skills)
        else:
            return Vacancy.objects.all()

    def update(self, request, *args, **kwargs):
        customer = request.user
        body = request.data
        vacancy_id = body['vacancy_id']
        flag = body['flag']

        if flag:
            favourite_vacancy = FavouriteVacancy.objects.get_or_create(customer=customer)[0]
            vacancy = Vacancy.objects.get(id=vacancy_id)

            if vacancy not in favourite_vacancy.vacancy.all():
                favourite_vacancy.vacancy.add(vacancy)
        else:
            try:
                favourite_vacancy = FavouriteVacancy.objects.get(customer=customer)
                is_exists = True
            except:
                is_exists = False

            if is_exists:
                vacancy = Vacancy.objects.get(id=vacancy_id)
                if vacancy in favourite_vacancy.vacancy.all():
                    favourite_vacancy.vacancy.remove(vacancy)

        queryset = Vacancy.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
