# Generated by Django 5.1.2 on 2024-10-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_alter_mobile_camera_resolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='PriceByDiscount',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='قیمت تخفیف خورده '),
        ),
    ]
