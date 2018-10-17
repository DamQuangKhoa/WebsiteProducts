# Generated by Django 2.1.2 on 2018-10-15 07:31

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surename', models.CharField(max_length=100)),
                ('add1', models.CharField(max_length=200)),
                ('add2', models.CharField(max_length=200)),
                ('add3', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('postcode', models.IntegerField(default=0)),
                ('registered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dilivery_addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surename', models.CharField(max_length=100)),
                ('add1', models.CharField(max_length=200)),
                ('add2', models.CharField(max_length=200)),
                ('add3', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('postcode', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Other_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanlity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.BooleanField(default=False)),
                ('payment_type', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=100)),
                ('total', models.IntegerField(default=0)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature.Customers')),
                ('delivery_add_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature.Dilivery_addresses')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='other_items',
            name='other_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature.Others'),
        ),
        migrations.AddField(
            model_name='other_items',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='feature.Products'),
        ),
    ]
