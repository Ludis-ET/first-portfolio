# Generated by Django 4.2.7 on 2023-11-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
