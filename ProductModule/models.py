from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from CarModule.models import CarModel

# Create your models here.

class ProductCategoryModel(models.Model):
    slug = models.CharField(max_length=300, editable=False, unique=True, null=True, verbose_name='دسته بندی در url')
    category = models.CharField(max_length=30, verbose_name='دسته بندی محصول')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        category_for_slug = self.category
        self.slug = slugify(category_for_slug, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندیِ محصول'
        verbose_name_plural = 'دسته بندی محصولات'

class ProductModel(models.Model):
    name = models.CharField(max_length=54, unique=True, verbose_name='نام محصول')
    cod = models.CharField(max_length=54, null=True, verbose_name='کد محصول')
    slug = models.SlugField(blank=True, null=True, editable=False, allow_unicode=True)
    country = models.CharField(max_length=54, null=True, verbose_name='کشور')
    price = models.CharField(max_length=30, verbose_name='قیمت محصول')
    price_integer = models.IntegerField(null=True, editable=False)
    category = models.ForeignKey(to=ProductCategoryModel, on_delete=models.CASCADE, verbose_name='دسته بندی محصول')
    car = models.ManyToManyField(CarModel, blank=True, verbose_name="خودرو")
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to='Media/product-images', null=True, verbose_name='تصویر محصول')
    brand = models.CharField(max_length=54, null=True, verbose_name='برند')
    show_on_main_page = models.BooleanField(default=False, verbose_name='قرار داشتن در خانه')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        title_for_slug = self.name
        self.slug = slugify(title_for_slug, allow_unicode=True)
        self.price_integer = int(self.price)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
