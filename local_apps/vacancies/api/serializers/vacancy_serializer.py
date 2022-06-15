from rest_framework import serializers
from local_apps.vacancies.models import Vacancy, FavouriteVacancy
from local_apps.users.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']


class VacancySerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    is_favourite = serializers.SerializerMethodField(method_name='get_favourite')

    def get_favourite(self, obj):
        customer = self.context.get('request', None).user
        try:
            favourite_vacancies = FavouriteVacancy.objects.get(customer=customer).vacancy.all()
        except:
            return False
        if obj in favourite_vacancies:
            return True
        else:
            return False

    class Meta:
        model = Vacancy
        fields = ['id', 'employer', 'title', 'created_on', 'description', 'link', 'final_salary', 'image_url',
                  'employment_type', 'schedule', 'specialization', 'location', 'skill', 'is_favourite']
