# Generated by Django 3.2.3 on 2021-06-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210609_1752'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.customer'),
        ),
    ]
