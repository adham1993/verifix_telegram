# Generated by Django 5.0.1 on 2024-03-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0026_candidate_chat_id_candidate_test_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='filial_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='login',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
