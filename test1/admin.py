from django.contrib import admin
from .models import Charactory, ProductCharactory, ProductMedia, Product, ProductPrice, Country, Manufactory, Category


admin.site.register([ProductCharactory, ProductMedia, Product, Charactory, ProductPrice, Country, Manufactory, Category])