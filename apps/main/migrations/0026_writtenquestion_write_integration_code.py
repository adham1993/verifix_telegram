# Generated by Django 5.0.1 on 2024-03-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_writtenanswer_write_integration_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='writtenquestion',
            name='write_integration_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
