from rest_framework.generics import RetrieveAPIView
from local_apps.users.models import Customer
from local_apps.users.api.serializers.register_serializer import UserSerializer

class UserInfoView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer