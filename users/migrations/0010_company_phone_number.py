# Generated by Django 2.2.6 on 2020-04-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200427_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.CharField(default='0587575884494', max_length=20),
            preserve_default=False,
        ),
    ]
