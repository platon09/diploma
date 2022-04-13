from django.urls import path
from .api.views.recommendation_view import RecommendationListView, RecommendationDetailView


urlpatterns = [
    path('', RecommendationListView.as_view()),
    path('<int:pk>/', RecommendationDetailView.as_view())
]