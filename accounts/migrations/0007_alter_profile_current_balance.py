# Generated by Django 5.1 on 2024-09-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_availiable_tarnsefere_profile_freehit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_balance',
            field=models.FloatField(default=12),
        ),
    ]
