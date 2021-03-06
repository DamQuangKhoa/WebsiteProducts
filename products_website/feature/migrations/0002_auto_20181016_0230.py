# Generated by Django 2.1.2 on 2018-10-16 02:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='other_items',
            old_name='other_id',
            new_name='other',
        ),
        migrations.RenameField(
            model_name='others',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='others',
            old_name='delivery_add_id',
            new_name='delivery',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='cat_id',
            new_name='cat',
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='dilivery_addresses',
            name='phone',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
