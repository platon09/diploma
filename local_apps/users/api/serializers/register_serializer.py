from rest_framework import serializers
from local_apps.users.models import Customer, Skill


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


# Skill serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


# User serializer
class UserSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField('get_skills_names')

    def get_skills_names(self, obj):
        out = []
        skills = obj.skill.all()
        for item in skills:
            out.append(SkillSerializer(item).data)
        return out

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'bio', 'info', 'image_url', 'skills')
