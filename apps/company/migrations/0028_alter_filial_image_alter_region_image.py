# Generated by Django 5.0.1 on 2024-03-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0027_company_filial_id_company_login_company_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/filials/images'),
        ),
        migrations.AlterField(
            model_name='region',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/regions/images'),
        ),
    ]
