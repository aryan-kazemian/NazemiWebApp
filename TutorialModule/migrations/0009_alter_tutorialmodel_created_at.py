# Generated by Django 5.1.5 on 2025-01-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorialModule', '0008_alter_tutorialmodel_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialmodel',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
