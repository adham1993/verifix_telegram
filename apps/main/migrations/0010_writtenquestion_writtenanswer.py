# Generated by Django 5.0.1 on 2024-02-25 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_userbot_resume_filter'),
        ('company', '0015_resumefilter_language_alter_candidate_add_date_and_more'),
        ('main', '0009_failedcandidate_education_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WrittenQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.TextField()),
                ('title_ru', models.TextField()),
                ('title_en', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='WrittenAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.TextField()),
                ('title_ru', models.TextField()),
                ('title_en', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.vacancy')),
                ('write_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.writtenquestion')),
            ],
        ),
    ]