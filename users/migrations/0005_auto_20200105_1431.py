# Generated by Django 2.2.6 on 2020-01-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200105_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='referrals',
            field=models.CharField(default='Hey there,how are you', max_length=40),
        ),
    ]
