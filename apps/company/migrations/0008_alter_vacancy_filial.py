# Generated by Django 5.0.1 on 2024-02-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_vacancy_company_alter_vacancy_filial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='filial',
            field=models.ManyToManyField(blank=True, related_name='vacancy_filial', to='company.filial'),
        ),
    ]
