# Generated by Django 3.2 on 2021-04-07 08:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('required_stars', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='QuestCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('stars', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('is_for_everyone', models.BooleanField(default=False, verbose_name='The Quest is for Everyone')),
                ('student1', models.CharField(blank=True, max_length=100, verbose_name='First Student')),
                ('student2', models.CharField(blank=True, max_length=100, verbose_name='Second Student')),
                ('student3', models.CharField(blank=True, max_length=100, verbose_name='Third Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='questboard.questboard')),
            ],
        ),
    ]
