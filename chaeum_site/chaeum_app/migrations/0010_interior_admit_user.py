# Generated by Django 3.2.13 on 2022-06-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaeum_app', '0009_interior_matching'),
    ]

    operations = [
        migrations.AddField(
            model_name='interior',
            name='admit_user',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]