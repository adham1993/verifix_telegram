# Generated by Django 5.0.1 on 2024-03-26 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_title_en_writtenanswer_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writtenanswer',
            old_name='integration_code',
            new_name='write_integration_code',
        ),
    ]
