# Generated by Django 4.2.1 on 2023-05-13 17:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_alter_category_options_alter_charactory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productprice', to='test1.product', verbose_name='Mahsulot'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='unit_name',
            field=models.UUIDField(default=uuid.UUID('669f3b42-2b69-4f7d-9d1b-48e156b5be96'), unique=True, verbose_name='Takrorlanmas_id'),
        ),
    ]
