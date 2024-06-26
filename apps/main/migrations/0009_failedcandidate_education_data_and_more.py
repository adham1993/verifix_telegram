# Generated by Django 5.0.1 on 2024-02-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_failedcandidate_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='failedcandidate',
            name='education_data',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='failedcandidate',
            name='language_data',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='successcandidate',
            name='education_data',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='successcandidate',
            name='language_data',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
