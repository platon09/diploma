from django.urls import path, include
from local_apps.roadmaps.api.views.specialization_view import SpecializationListView
from local_apps.roadmaps.api.views.technology_view import TechnologyListView, RecordProgressView
from local_apps.roadmaps.api.views.topic_view import TopicListView, TopicDetailView


urlpatterns = [
    path('', SpecializationListView.as_view()),
    path('<int:id>/', include([
        path('', TechnologyListView.as_view()),
        path('<int:id>/', include([
            path('', TopicListView.as_view()),
            path('done/', RecordProgressView.as_view()),
            path('<int:id>/', include([
                path('', TopicDetailView.as_view())
            ])),
        ])),
    ])),
]
