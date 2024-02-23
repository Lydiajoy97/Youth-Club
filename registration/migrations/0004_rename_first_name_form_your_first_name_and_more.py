# Generated by Django 4.2.10 on 2024-02-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_form_date_of_birth_form_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='first_name',
            new_name='your_first_name',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='last_name',
            new_name='your_last_name',
        ),
        migrations.AddField(
            model_name='form',
            name='childs_name',
            field=models.CharField(default='Name', max_length=200),
        ),
    ]
