# Generated by Django 3.0.8 on 2022-05-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaeum_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='star_address',
            field=models.TextField(default=''),
        ),
    ]