# Generated by Django 4.2.7 on 2023-11-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_me_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
