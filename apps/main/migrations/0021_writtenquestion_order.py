# Generated by Django 5.0.1 on 2024-03-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_question_vacancy_question_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='writtenquestion',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
