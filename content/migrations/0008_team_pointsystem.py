# Generated by Django 5.1 on 2024-09-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_player_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='pointsystem',
            field=models.JSONField(default={'pointsystem': []}),
        ),
    ]
