# Generated by Django 4.2.6 on 2023-10-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Под заказ')], max_length=50),
        ),
    ]
