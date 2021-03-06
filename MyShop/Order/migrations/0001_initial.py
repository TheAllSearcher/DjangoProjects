# Generated by Django 3.1.4 on 2020-12-31 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket', related_query_name='basket', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(verbose_name='create at')),
                ('update_at', models.DateTimeField(verbose_name='update at')),
                ('description', models.TextField(verbose_name='description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', related_query_name='order', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', related_query_name='payment', to='Order.order', verbose_name='order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', related_query_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='count')),
                ('price', models.IntegerField(verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItem', related_query_name='orderItem', to='Order.order', verbose_name='order')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='Product.shopproduct', verbose_name='shop_product')),
            ],
            options={
                'verbose_name': 'orderItem',
                'verbose_name_plural': 'orderItems',
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='price')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basketItem', related_query_name='basketItem', to='Order.basket', verbose_name='basket')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basketItem', related_query_name='basketItem', to='Product.shopproduct', verbose_name='shop_product')),
            ],
            options={
                'verbose_name': 'basketItem',
                'verbose_name_plural': 'basketItems',
            },
        ),
    ]
