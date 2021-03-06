# Generated by Django 2.2.4 on 2019-08-02 11:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('street', models.CharField(blank=True, max_length=120, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=120, null=True)),
                ('stateOrProvince', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('telephone', models.CharField(blank=True, max_length=120, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myrestaurant')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='myrestaurant.Restaurant')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.Restaurant')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('restaurant', 'user')},
            },
        ),
    ]
