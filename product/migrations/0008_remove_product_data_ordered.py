# Generated by Django 3.2.3 on 2021-06-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210609_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='data_ordered',
        ),
    ]
