# Generated by Django 2.2.6 on 2020-05-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_order_pay_on_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reference_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]