# Generated by Django 4.2.10 on 2024-06-28 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activites', '0003_alter_activityform_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityform',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
