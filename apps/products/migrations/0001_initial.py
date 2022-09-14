# Generated by Django 4.1 on 2022-09-14 12:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='JoinUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'JoinedUser',
                'db_table': 'joined_users',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, 'Product should have minimal 5 score'), django.core.validators.MinValueValidator(1, 'Product should have maximal 1 score')])),
                ('size', models.CharField(choices=[('S', 'Size S'), ('M', 'Size M'), ('L', 'Size L'), ('XL', 'Size Xl')], default='S', max_length=25)),
                ('tag', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product')),
            ],
            options={
                'verbose_name_plural': 'ProductImage',
                'db_table': 'product_image',
            },
        ),
    ]
