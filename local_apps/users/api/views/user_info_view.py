from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from local_apps.users.api.serializers.register_serializer import UserSerializer
from rest_framework.response import Response


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
