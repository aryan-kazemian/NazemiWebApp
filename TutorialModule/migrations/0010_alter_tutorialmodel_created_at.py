# Generated by Django 5.1.5 on 2025-01-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorialModule', '0009_alter_tutorialmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
