# Generated by Django 5.0.4 on 2024-05-06 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_cartmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartmodel',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
    ]
