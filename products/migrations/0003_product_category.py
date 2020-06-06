# Generated by Django 2.2.6 on 2020-03-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200328_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SMALL', 'Small package'), ('JUMBO', 'Jumbo package')], default='SMALL', max_length=10),
            preserve_default=False,
        ),
    ]