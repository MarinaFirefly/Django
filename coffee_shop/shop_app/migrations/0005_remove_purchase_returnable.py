# Generated by Django 3.0.3 on 2020-03-19 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_auto_20200319_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='returnable',
        ),
    ]
