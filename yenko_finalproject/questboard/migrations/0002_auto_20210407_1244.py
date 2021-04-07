# Generated by Django 3.2 on 2021-04-07 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questboard',
            old_name='is_for_all',
            new_name='is_for_everyone',
        ),
        migrations.AlterField(
            model_name='questboard',
            name='student1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='questboard',
            name='student2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='questboard',
            name='student3',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]