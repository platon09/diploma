from rest_framework import serializers
from local_apps.users.models import Customer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create_user(password=validated_data['password'],
                                            email=validated_data['email'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
