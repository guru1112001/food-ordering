# Generated by Django 4.0.6 on 2023-01-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_cart_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_info',
            name='product',
            field=models.ManyToManyField(to='ordering.product'),
        ),
    ]
