# Generated by Django 5.1.5 on 2025-01-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorialModule', '0010_alter_tutorialmodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialmodel',
            name='show_on_main',
            field=models.BooleanField(default=False, verbose_name='نشان دادن در خانه'),
        ),
    ]
