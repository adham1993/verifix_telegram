# Generated by Django 5.0.1 on 2024-02-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_candidate_wage_expectation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='filial',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='filial',
            field=models.ManyToManyField(to='company.filial'),
        ),
    ]
