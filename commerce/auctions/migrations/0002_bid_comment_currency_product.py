# Generated by Django 3.2.6 on 2021-09-10 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sign', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='auctions.currency')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=64)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owners', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='auctions.product')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_currencies', to='auctions.currency')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
