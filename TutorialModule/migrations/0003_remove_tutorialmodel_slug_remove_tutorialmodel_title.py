# Generated by Django 5.1.5 on 2025-01-31 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TutorialModule', '0002_alter_tutorialmodel_options_tutorialmodel_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tutorialmodel',
            name='title',
        ),
    ]
