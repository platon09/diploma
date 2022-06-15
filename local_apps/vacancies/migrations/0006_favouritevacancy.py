# Generated by Django 4.0.3 on 2022-06-15 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0005_alter_vacancy_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_vacancy', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ManyToManyField(related_name='favourite_vacancy', to='vacancies.vacancy')),
            ],
            options={
                'verbose_name': 'Favourite Vacancy',
                'verbose_name_plural': 'Favourite Vacancies',
            },
        ),
    ]
