from django.urls import path, include
from local_apps.roadmaps.api.views.specialization_view import SpecializationListView, SpecializationDetailView
from local_apps.roadmaps.api.views.section_view import SectionListView
from local_apps.roadmaps.api.views.topic_view import TopicListView, TopicDetailView
from local_apps.roadmaps.api.views.subtopic_view import SubTopicListView


urlpatterns = [
    path('', SpecializationListView.as_view()),
    path('<slug:spec_slug>/', include([
        path('', SpecializationDetailView.as_view()),
        path('sections/', SectionListView.as_view()),
        path('sections/<slug:section_slug>/', include([
            path('', TopicListView.as_view()),
            path('<slug:topic_slug>/', include([
                path('',  TopicDetailView.as_view()),
                path('subtopics/', SubTopicListView.as_view())
            ])),
        ])),
    ])),
]