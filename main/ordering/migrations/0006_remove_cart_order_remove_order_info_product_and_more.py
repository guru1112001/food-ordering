# Generated by Django 4.0.6 on 2023-01-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0005_order_info_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order_info',
            name='product',
        ),
        migrations.AddField(
            model_name='order_info',
            name='products',
            field=models.ManyToManyField(to='ordering.cart'),
        ),
        migrations.AlterField(
            model_name='order_info',
            name='take_away',
            field=models.BooleanField(default=False),
        ),
    ]
