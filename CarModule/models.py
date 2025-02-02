from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.


class CarModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='خودرو')
    slug = models.SlugField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to='Media/CarImages', verbose_name='تصویر خودرو')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    show_on_main = models.BooleanField(default=False, verbose_name='نشان دادن در خانه')

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        title_for_slug = unidecode(self.name)
        self.slug = slugify(title_for_slug)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'خودرو'
        verbose_name_plural = 'خودروها'