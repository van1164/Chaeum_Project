# Generated by Django 3.2.13 on 2022-06-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaeum_app', '0008_auto_20220521_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='interior',
            name='matching',
            field=models.BooleanField(default=False),
        ),
    ]