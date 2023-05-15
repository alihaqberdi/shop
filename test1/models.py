from django.db import models

# Create your models here.


from django.db import models
from uuid import uuid4


class Country(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Davlat'

    def __str__(self):
        return self.name


class Manufactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')
    description = models.TextField(verbose_name='Haqida')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Ishlab chiqligan')

    class Meta:
        verbose_name_plural = 'Ishlab Chiqqan Zavod'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Categoriya'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Kategoriya')
    manufactory = models.ForeignKey(Manufactory, on_delete=models.PROTECT, related_name='manufactory',
                                    verbose_name='Ishlab chiqqan Korxona')  # verbose_name
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Ishlab chiqligan davlat')
    sale_count = models.DecimalField(max_digits=17, decimal_places=2, default=0, verbose_name='Skidka Narxi')
    view_count = models.PositiveBigIntegerField(default=0, verbose_name='Ko\'rganlar soni')
    is_active = models.BooleanField(default=True, verbose_name='Holati Aktiv')

    class Meta:
        verbose_name_plural = 'Mahsulot'

    def __str__(self):
        return self.name


class Charactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Xil(xususiyat)'

    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    product = models.ForeignKey(Product, models.PROTECT, verbose_name='Mahsulot', related_name='productmedia')
    media = models.FileField(upload_to='product/media', verbose_name='Video/Rasm')
    is_active = models.BooleanField(default=True, verbose_name='Holati Aktiv')

    class Meta:
        verbose_name_plural = 'Mahsulot Video/rasmlari'

    def __str__(self):
        return self.product.name


class ProductCharactory(models.Model):
    product = models.ForeignKey(Product, models.PROTECT, verbose_name='Mahsulot', related_name='productcharactory')
    charactory = models.ForeignKey(Charactory, models.PROTECT, verbose_name='Mahsulot xususiyati')
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Mahsulot xususiyati'

    def __str__(self):
        return self.product.name


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, models.PROTECT, verbose_name='Mahsulot', related_name='productprice')
    unit_name = models.UUIDField(default=uuid4(), verbose_name='Takrorlanmas_id', unique=True)
    price = models.DecimalField(max_digits=17, decimal_places=2, default=0, verbose_name='Narxi')
    is_active = models.BooleanField(default=True, verbose_name='Holati Aktiv')

    class Meta:
        verbose_name_plural = 'Mahsulot Narxlari'

    def __str__(self):
        return self.product.name
