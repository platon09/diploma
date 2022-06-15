from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from local_apps.users.api.serializers.register_serializer import UserSerializer

from local_apps.users.models import Customer


class CustomJwtTokenView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        customer = Customer.objects.get(email=request.data['email'])

        response_data = {
            'user': UserSerializer(customer).data,
            'data': serializer.validated_data
        }

        return Response(response_data, status=status.HTTP_200_OK)