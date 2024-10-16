# Generated by Django 5.1.2 on 2024-10-10 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_alter_mobile_options_alter_mobile_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile_Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Networks', models.CharField(max_length=5, verbose_name='شبکه موبایل')),
            ],
            options={
                'verbose_name': 'شبکه موبایل',
                'verbose_name_plural': 'شبکه موبایل',
            },
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pro_Network', to='Shop.mobile_network', verbose_name='شبکه'),
        ),
    ]
