# Generated by Django 5.0.1 on 2024-02-28 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_userbot_write_answer_userbot_write_number_and_more'),
        ('company', '0016_candidatelanguages_company_and_more'),
        ('main', '0012_writtenanswer_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile'),
        ),
        migrations.AddField(
            model_name='education',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.vacancy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile'),
        ),
        migrations.AddField(
            model_name='language',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.vacancy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='languagelevel',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile'),
        ),
        migrations.AddField(
            model_name='languagelevel',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.vacancy'),
            preserve_default=False,
        ),
    ]
