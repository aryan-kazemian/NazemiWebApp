# Generated by Django 5.1.5 on 2025-01-31 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CarModule', '0004_carmodel_show_on_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(editable=False, max_length=300, null=True, unique=True, verbose_name='دسته بندی در url')),
                ('category', models.CharField(max_length=30, verbose_name='دسته بندی محصول')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'دسته بندیِ محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54, unique=True, verbose_name='نام محصول')),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('price', models.CharField(max_length=30, verbose_name='قیمت محصول')),
                ('price_integer', models.IntegerField(editable=False, null=True)),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('main_image', models.ImageField(null=True, upload_to='media/product-images', verbose_name='تصویر محصول')),
                ('show_on_main_page', models.BooleanField(default=False, verbose_name='قرار داشتن در خانه')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('car', models.ManyToManyField(blank=True, to='CarModule.carmodel', verbose_name='خودرو')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductModule.productcategorymodel', verbose_name='دسته بندی محصول')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
