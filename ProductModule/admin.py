from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ProductModel)
admin.site.register(models.ProductCategoryModel)