# Generated by Django 4.0.5 on 2022-08-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='category', related_query_name='category', to='products.category'),
        ),
    ]
