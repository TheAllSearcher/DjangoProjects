# Generated by Django 3.1.4 on 2020-12-31 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('detail', models.TextField(help_text='Enter Your Brand Detail', verbose_name='Detail')),
                ('image', models.ImageField(upload_to='brand/image/', verbose_name='Image')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('detail', models.TextField(blank=True, help_text='Enter Your Category Detail', verbose_name='Detail')),
                ('image', models.ImageField(upload_to='category/image/', verbose_name='Image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', related_query_name='children', to='Product.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Off',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('image', models.ImageField(upload_to='product/image/', verbose_name='Image')),
                ('detail', models.CharField(max_length=150, verbose_name='Detail')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', related_query_name='Product', to='Product.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', related_query_name='Product', to='Product.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
                ('quantity', models.CharField(max_length=50, verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Product.product', verbose_name='Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Account.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'shop_product',
                'verbose_name_plural': 'shops_products',
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductMeta', related_query_name='ProductMeta', to='Product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'product_meta',
                'verbose_name_plural': 'product_metas',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.BooleanField(verbose_name='Condition')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='Product.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', related_query_name='like', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/image/', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image', related_query_name='Image', to='Product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='Enter Your Comment', verbose_name='Text')),
                ('rate', models.IntegerField(blank=True, verbose_name='Rate')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', related_query_name='Comment', to='Product.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', related_query_name='Comment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
