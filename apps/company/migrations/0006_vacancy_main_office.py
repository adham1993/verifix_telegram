# Generated by Django 5.0.1 on 2024-02-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_vacancy_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='main_office',
            field=models.BooleanField(default=False),
        ),
    ]
