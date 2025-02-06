from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.

class TutorialModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='سر تیتر', unique=True, null=True)
    slug = models.SlugField(blank=True, null=True, editable=False, allow_unicode=True)
    text = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='Media/Tutorial-images', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    writer = models.CharField(max_length=200, verbose_name='نویسنده', null=True)
    show_on_main = models.BooleanField(default=False, verbose_name='نشان دادن در خانه')
    minutes_to_read = models.IntegerField(default=5, verbose_name="چند دقیقه برای مطالعه نیاز است ؟")

    def save(self, *args, **kwargs):
        category_for_slug = self.title
        self.slug = slugify(category_for_slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'آموزش'
        verbose_name_plural = 'آموزش‌ها'
