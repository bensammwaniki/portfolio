# Generated by Django 4.0 on 2021-12-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_testmonials_image_name_testmonials_testmony'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmonials',
            name='position',
            field=models.TextField(null=True),
        ),
    ]
