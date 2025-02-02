# Generated by Django 5.1.5 on 2025-01-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeModule', '0004_quicklinkmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='تیتر اسلایدر')),
                ('text', models.TextField(verbose_name='متن اسلایدر')),
                ('image', models.ImageField(upload_to='Media/logo', verbose_name='تصویر')),
                ('button_text', models.CharField(max_length=200, verbose_name='تیتر کلید')),
                ('button_link', models.URLField()),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
    ]
