# Generated by Django 4.0.4 on 2022-06-05 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_order_totalprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='score',
        ),
        migrations.AddField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
    ]
