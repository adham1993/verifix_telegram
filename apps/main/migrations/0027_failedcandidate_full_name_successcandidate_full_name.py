# Generated by Django 5.0.1 on 2024-03-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_writtenquestion_write_integration_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='failedcandidate',
            name='full_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='successcandidate',
            name='full_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
