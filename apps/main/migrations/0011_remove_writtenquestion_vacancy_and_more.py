# Generated by Django 5.0.1 on 2024-02-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_resumefilter_language_alter_candidate_add_date_and_more'),
        ('main', '0010_writtenquestion_writtenanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writtenquestion',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='writtenquestion',
            name='vacancy',
            field=models.ManyToManyField(to='company.vacancy'),
        ),
    ]
