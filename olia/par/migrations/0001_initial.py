# Generated by Django 5.0.6 on 2024-07-06 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('accredited', models.BooleanField(default=False)),
                ('trusted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalRole',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10000)),
                ('url', models.CharField(max_length=10000)),
                ('salary_from', models.IntegerField()),
                ('salary_to', models.IntegerField()),
                ('salary_currency', models.CharField(max_length=100)),
                ('salary_gross', models.IntegerField()),
                ('vacancy_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('requirements', models.TextField()),
                ('responsibilities', models.TextField()),
                ('experience', models.TextField()),
                ('employment', models.TextField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='par.area')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='par.employer')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='par.professionalrole')),
            ],
        ),
    ]
