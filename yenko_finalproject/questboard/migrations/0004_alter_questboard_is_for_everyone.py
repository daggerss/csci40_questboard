# Generated by Django 3.2 on 2021-04-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0003_auto_20210407_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questboard',
            name='is_for_everyone',
            field=models.BooleanField(default=False, verbose_name='The quest is for everyone'),
        ),
    ]