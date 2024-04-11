# Generated by Django 4.2.6 on 2024-04-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryMedicalConsultations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.CharField(max_length=50, verbose_name='Médico')),
                ('date_start', models.CharField(max_length=50, verbose_name='Fecha - Hora/inicio consulta')),
                ('date_end', models.CharField(max_length=50, verbose_name='Fecha - Hora/Termino consulta')),
                ('incidents', models.CharField(max_length=50, verbose_name='Incidencias')),
                ('user', models.CharField(max_length=50, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Consultas del dia',
            },
        ),
    ]