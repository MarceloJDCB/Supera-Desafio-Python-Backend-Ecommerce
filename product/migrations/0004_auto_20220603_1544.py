# Generated by Django 3.1.4 on 2022-06-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
