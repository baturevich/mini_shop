# Generated by Django 3.1.3 on 2020-11-05 20:25

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201105_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=home.models.product_image_directory_path, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.products', verbose_name='Продукт'),
        ),
    ]
