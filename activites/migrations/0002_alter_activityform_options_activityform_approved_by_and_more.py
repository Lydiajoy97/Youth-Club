# Generated by Django 4.2.10 on 2024-07-09 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activityform',
            options={'ordering': ['updated_on']},
        ),
        migrations.AddField(
            model_name='activityform',
            name='approved_by',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activityform',
            name='author',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='addactivity', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activityform',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityform',
            name='first_name',
            field=models.CharField(default='id', max_length=200),
        ),
        migrations.AlterField(
            model_name='activityform',
            name='game_ideas',
            field=models.TextField(),
        ),
    ]
