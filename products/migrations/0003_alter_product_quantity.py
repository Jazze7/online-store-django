# Generated by Django 4.2.1 on 2023-05-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
