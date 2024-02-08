# Generated by Django 5.0.1 on 2024-02-07 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_userbot_filial_userbot_region'),
        ('content', '0005_filialmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.TextField()),
                ('title_ru', models.TextField()),
                ('title_en', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/region_message/images')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.userprofile')),
            ],
            options={
                'verbose_name': 'Filial text',
                'verbose_name_plural': 'Filial text',
            },
        ),
    ]
