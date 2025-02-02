from django.db import models

# Create your models here.

class SiteSettingsModel(models.Model):
    shop_name = models.CharField(max_length=120, verbose_name="نام قروشگاه")
    logo = models.ImageField(upload_to='Media/logo', verbose_name='لوگو')
    phone_number = models.CharField(max_length=20, verbose_name='شماره تماس')
    address = models.CharField(max_length=300, verbose_name='آدرس فروشگاه')
    about_us_title = models.CharField(max_length=200, verbose_name='تیتر درباره ما')
    about_us_text = models.TextField(verbose_name='متن درباره ما')
    contact_us_text = models.TextField(verbose_name='متن تماس با ما', null=True)
    copy_right_text = models.TextField(verbose_name="متن کپی رایت")
    whatsapp_phone_number = models.URLField(verbose_name='شماره واتساپ', null=True)
    telegram_phone_number = models.URLField(verbose_name='شماره تلگرام', null=True)
    email = models.EmailField(verbose_name="ایمیل", null=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')


    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

class QuickLinkModel(models.Model):
    name = models.CharField(max_length=60, verbose_name="نام")
    link = models.URLField()
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "لینک‌ سریع"
        verbose_name_plural ="لینک‌های سریع"

class SliderModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='تیتر اسلایدر')
    text = models.TextField(verbose_name='متن اسلایدر')
    image = models.ImageField(upload_to='Media/logo', verbose_name='تصویر')
    button_text =  models.CharField(max_length=200, verbose_name='تیتر کلید')
    button_link = models.URLField()
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural ="اسلایدرها"

