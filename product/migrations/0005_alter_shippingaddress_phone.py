# Generated by Django 3.2.3 on 2021-06-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210602_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
