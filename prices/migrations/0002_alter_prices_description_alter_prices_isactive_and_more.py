# Generated by Django 4.2.6 on 2024-03-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='isActive',
            field=models.BooleanField(verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Precio'),
        ),
    ]
