# Generated by Django 3.2.7 on 2021-09-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenward', '0002_local_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='website',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
