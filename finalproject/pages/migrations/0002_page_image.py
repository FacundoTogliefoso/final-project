# Generated by Django 3.2.4 on 2021-06-08 02:55

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pages.models.custom_upload_to),
        ),
    ]