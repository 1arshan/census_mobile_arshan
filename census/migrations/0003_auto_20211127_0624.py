# Generated by Django 3.2.9 on 2021-11-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0002_child_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='father_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='child',
            name='mother_name',
            field=models.CharField(max_length=60),
        ),
    ]
