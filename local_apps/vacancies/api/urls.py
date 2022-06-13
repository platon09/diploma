from django.urls import path
from local_apps.vacancies.api.views.vacancy_view import VacancyListView, VacancyDetailView


urlpatterns = [
    path('', VacancyListView.as_view()),
    path('<int:pk>/', VacancyDetailView.as_view())
]
