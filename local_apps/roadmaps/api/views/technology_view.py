import json

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from local_apps.users.models import Customer
from local_apps.roadmaps.models import Specialization, Technology, UserStudy
from local_apps.roadmaps.api.serializers.technology_serializer import TechnologySerializer


class TechnologyListView(ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        pk = self.kwargs['spec_id']
        technology_qs = Specialization.objects.get(id=pk).technologies.all()
        return technology_qs


class RecordProgressView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        is_done = json.loads(request.query_params.get('done'))
        customer = request.user
        tech_id = kwargs['tech_id']

        tech = Technology.objects.get(id=tech_id)
        userstudy = UserStudy.objects.get_or_create(user=customer, technology=tech)[0]
        num_topics = tech.topics.count()
        percent = 100 / num_topics

        if is_done:
            if userstudy.progress < 100:
                userstudy.progress += percent
                userstudy.save()
                userstudy_progress = userstudy.progress
                if userstudy_progress < 100:
                    return Response(f"Progress of {request.user.full_name} recorded: {round(userstudy.progress)}%. Added +{round(percent)}% to progress.")
                elif userstudy_progress >= 100:
                    customer.skill.add(*tech.skill.all().values_list('id', flat=True))
                    return Response(f"Congratulations, you've learned enough about {userstudy.technology.name} technology!")
        else:
            if userstudy.progress > 0:
                userstudy.progress -= percent
                userstudy.save()
                return Response(f"Progress of {request.user.full_name} changed: {round(userstudy.progress)}%. Subtracted -{round(percent)} from progress")
