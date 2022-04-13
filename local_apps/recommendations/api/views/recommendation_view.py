from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from local_apps.recommendations.models import Recommendation
from local_apps.recommendations.api.serializers.recommendation_serializer import RecommendationSerializer


class RecommendationListView(ListAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


class RecommendationDetailView(RetrieveAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_object(self):
        recommendation = Recommendation.objects.get(id=self.kwargs['pk'])
        return recommendation

    def retrieve(self, request, *args, **kwargs):
        recommendation = Recommendation.objects.filter(id=self.kwargs['pk'])
        if not recommendation:
            raise ValidationError(detail='Recommendation is not found', code=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
