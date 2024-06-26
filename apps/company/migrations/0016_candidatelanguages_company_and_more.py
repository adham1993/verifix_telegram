# Generated by Django 5.0.1 on 2024-02-28 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_userbot_write_answer_userbot_write_number_and_more'),
        ('company', '0015_resumefilter_language_alter_candidate_add_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatelanguages',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='candidatelanguages',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_candidate_language', to='bot.userprofile'),
        ),
        migrations.AddField(
            model_name='region',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='region',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_region', to='bot.userprofile'),
        ),
    ]
