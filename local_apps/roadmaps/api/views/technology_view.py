import json

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from local_apps.roadmaps.models import Techstack, Topic, UserStudy
from local_apps.roadmaps.api.serializers.technology_serializer import TechnologySerializer


class TechnologyListView(ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        technology_qs = Techstack.objects.get(id=pk).technology.all()
        return technology_qs


class RecordProgressView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        is_done = json.loads(request.query_params.get('done'))
        customer = request.user
        tech_slug = kwargs['tech_slug']

        userstudy = UserStudy.objects.get_or_create(user=customer, technology__slug=tech_slug)
        num_topics = Topic.objects.filter(technology__slug=tech_slug).count()
        percent = 100 / num_topics

        if is_done:
            if userstudy.progress < 100:
                userstudy.progress += percent
                userstudy.save()
                userstudy_progress = userstudy.progress
                if userstudy_progress != 100:
                    return Response(f"Progress of {request.user.full_name} recorded: {round(userstudy.progress)}%. Added +{round(percent)}% to progress.")
        else:
            if userstudy.progress > 0:
                userstudy.progress -= percent
                userstudy.save()
                return Response(f"Progress of {request.user.full_name} changed: {round(userstudy.progress)}%. Subtracted -{round(percent)} from progress")
