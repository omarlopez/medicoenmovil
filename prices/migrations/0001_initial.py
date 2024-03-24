# Generated by Django 4.2.6 on 2024-03-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('isActive', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Precios',
            },
        ),
    ]
