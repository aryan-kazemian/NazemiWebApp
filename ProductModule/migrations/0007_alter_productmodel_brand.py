# Generated by Django 5.1.5 on 2025-01-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductModule', '0006_productmodel_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='brand',
            field=models.CharField(max_length=54, null=True, verbose_name='برند'),
        ),
    ]
