# Generated by Django 4.2.10 on 2024-06-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activites', '0004_activityform_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityform',
            name='game_ideas',
            field=models.TextField(),
        ),
    ]
