# Generated by Django 4.2.6 on 2024-04-02 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statusCatalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Doctor')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='statusCatalog.catalogstatus', verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Mi Actividad',
            },
        ),
    ]
