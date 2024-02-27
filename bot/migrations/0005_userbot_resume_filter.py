# Generated by Django 5.0.1 on 2024-02-24 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_userbot_answer_userbot_q_number_userbot_question_and_more'),
        ('company', '0013_alter_resumefilter_bot_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbot',
            name='resume_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.resumefilter'),
        ),
    ]