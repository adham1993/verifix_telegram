# Generated by Django 5.0.1 on 2024-02-18 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_vacancy_filial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.region'),
        ),
    ]