# Generated by Django 3.0.3 on 2020-03-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_auto_20200322_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]