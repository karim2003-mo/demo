# Generated by Django 5.1 on 2024-09-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='score',
        ),
        migrations.AddField(
            model_name='profile',
            name='leagues',
            field=models.JSONField(default={'leagues': []}),
        ),
        migrations.AddField(
            model_name='profile',
            name='squad',
            field=models.JSONField(default={'squad': []}),
        ),
    ]