# Generated by Django 5.1 on 2024-08-31 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('founded_at', models.DateField(blank=True, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
                ('coach', models.CharField(blank=True, max_length=30, null=True)),
                ('leagues', models.IntegerField(blank=True, null=True)),
                ('local_cup', models.IntegerField(blank=True, null=True)),
                ('local_super', models.IntegerField(blank=True, null=True)),
                ('continental_cups', models.CharField(blank=True, max_length=30, null=True)),
                ('squad', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('birht_date', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('position', models.CharField(blank=True, choices=[('Gk', 'Gk'), ('Lb', 'Lb'), ('cb', 'cb'), ('Rb', 'Rb'), ('Dmf', 'Dmf'), ('Cmf', 'Cmf'), ('Amf', 'Amf'), ('Lwf', 'Lwf'), ('Rwf', 'Rwf'), ('Ss', 'Ss'), ('Cf', 'Cf')], max_length=30, null=True)),
                ('goals', models.IntegerField(blank=True, null=True)),
                ('assist', models.IntegerField(blank=True, null=True)),
                ('clean_sheet', models.IntegerField(blank=True, null=True)),
                ('yellow_card', models.IntegerField(blank=True, null=True)),
                ('red_card', models.IntegerField(blank=True, null=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='content.team')),
            ],
        ),
    ]