# Generated by Django 3.2.8 on 2021-10-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_image_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
