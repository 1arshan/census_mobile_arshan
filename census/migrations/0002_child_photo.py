# Generated by Django 3.2.9 on 2021-11-26 15:44

import census.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='photo',
            field=models.ImageField(blank=True, upload_to=census.models.renaming_uploaded_file1),
        ),
    ]
