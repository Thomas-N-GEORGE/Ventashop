# Generated by Django 4.2 on 2023-04-14 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventashop', '0008_alter_lineitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventashop.cart'),
        ),
    ]
