from .models import Country, Manufactory, Category, Product, Charactory, ProductMedia, ProductCharactory, ProductPrice
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CountrySerializers(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ManufactorySerializers(ModelSerializer):
    country = CountrySerializers(read_only=True)

    class Meta:
        model = Manufactory
        fields = '__all__'


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductMediaSerializers(ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductMedia
        fields = '__all__'


class CharactorySerializers(ModelSerializer):
    class Meta:
        model = Charactory
        fields = '__all__'


class ProductCharactorySerializers(ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductCharactory
        fields = '__all__'



class ProductPriceSerializers(ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductPrice
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    country = CountrySerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    manufactory = ManufactorySerializers(read_only=True)
    productmedia = ProductMediaSerializers(many=True, read_only=True)
    productcharactory = ProductCharactorySerializers(many=True, read_only=True)
    productprice = ProductPriceSerializers(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'category', 'manufactory', 'country', 'sale_count', 'view_count','productmedia','productcharactory',
                  'is_active', 'productprice']


