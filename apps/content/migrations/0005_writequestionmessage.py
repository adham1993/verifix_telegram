# Generated by Django 5.0.1 on 2024-02-26 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_userbot_resume_filter'),
        ('content', '0004_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteQuestionMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.TextField()),
                ('title_ru', models.TextField()),
                ('title_en', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/write_question_message/images')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile')),
            ],
            options={
                'verbose_name': 'Write Question text',
                'verbose_name_plural': 'Write Question text',
            },
        ),
    ]
