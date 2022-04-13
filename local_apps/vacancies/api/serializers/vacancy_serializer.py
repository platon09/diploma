from rest_framework import serializers
from local_apps.vacancies.models import Vacancy
from local_apps.users.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']


class VacancySerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'created_on', 'description', 'salary', 'image_url', 'employment_type', 'schedule', 'specialization', 'location', 'skill']
