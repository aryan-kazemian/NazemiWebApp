# Generated by Django 5.1.5 on 2025-01-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductModule', '0002_alter_productmodel_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='cod',
            field=models.CharField(max_length=54, null=True, verbose_name='کد محصول'),
        ),
    ]
