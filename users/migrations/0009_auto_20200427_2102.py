# Generated by Django 2.2.6 on 2020-04-27 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20200105_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=300)),
                ('farm_name', models.CharField(blank=True, max_length=200, null=True)),
                ('major_products', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Farmers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Students',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
