# Generated by Django 4.2 on 2023-04-14 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventashop', '0005_cart_lineitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cart', to='ventashop.cart'),
        ),
    ]
