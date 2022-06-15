from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from local_apps.users.api.serializers.register_serializer import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "data":
                    {
                        "refresh": refresh,
                        "access": access
                    },
            }
        )
