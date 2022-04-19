from django.urls import path
from .api.views.vacancy_view import VacancyListView, VacancyDetailView


urlpatterns = [
    path('', VacancyListView.as_view()),
    path('<int:pk>/', VacancyDetailView.as_view())
]
