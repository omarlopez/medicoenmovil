# Generated by Django 4.2.6 on 2024-03-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fullName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('secondLastName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cedProf', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('isActive', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Doctores',
            },
        ),
    ]
