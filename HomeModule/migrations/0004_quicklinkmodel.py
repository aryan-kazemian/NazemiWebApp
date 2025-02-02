# Generated by Django 5.1.5 on 2025-01-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeModule', '0003_remove_footerlinksmodel_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickLinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='نام')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'لینک\u200c سریع',
                'verbose_name_plural': 'لینک\u200cهای سریع',
            },
        ),
    ]
