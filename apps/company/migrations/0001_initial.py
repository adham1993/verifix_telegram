# Generated by Django 5.0.1 on 2024-02-17 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True)),
                ('gender', models.CharField(blank=True, max_length=128, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/candidate/images')),
                ('main_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('extra_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('legal_address', models.CharField(blank=True, max_length=256, null=True)),
                ('wage_expectation', models.IntegerField(blank=True, default=0, null=True)),
                ('node', models.CharField(blank=True, max_length=256, null=True)),
                ('bot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_user', to='bot.userbot')),
                ('education', models.ManyToManyField(blank=True, to='main.education')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_candidate', to='bot.userprofile')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_languages', to='company.candidate')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('language_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.languagelevel')),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128)),
                ('name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('name_en', models.CharField(blank=True, max_length=128, null=True)),
                ('opened_date', models.DateTimeField(auto_now=True)),
                ('closed_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_filial', to='bot.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='filial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.filial'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128)),
                ('name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('name_en', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='company.region')),
            ],
        ),
        migrations.AddField(
            model_name='filial',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.region'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.region'),
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128)),
                ('name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('name_en', models.CharField(blank=True, max_length=128, null=True)),
                ('description_uz', models.TextField()),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('job_name_uz', models.CharField(max_length=128)),
                ('job_name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('job_name_en', models.CharField(blank=True, max_length=128, null=True)),
                ('schedule_uz', models.TextField(verbose_name='Work time uzbek')),
                ('schedule_ru', models.TextField(blank=True, null=True, verbose_name='Work time russian')),
                ('schedule_en', models.TextField(blank=True, null=True, verbose_name='Work time english')),
                ('wage_limit_uz', models.TextField(verbose_name='salary work uzbek')),
                ('wage_limit_ru', models.TextField(blank=True, null=True, verbose_name='salary work russian')),
                ('wage_limit_en', models.TextField(blank=True, null=True, verbose_name='salary work english')),
                ('lang_uz', models.CharField(max_length=64, verbose_name='Tillar')),
                ('lang_ru', models.CharField(blank=True, max_length=64, null=True, verbose_name='Languages')),
                ('lang_en', models.CharField(blank=True, max_length=64, null=True, verbose_name='Язикы')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.filial')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.region')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_vacancy', to='bot.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.vacancy'),
        ),
    ]
