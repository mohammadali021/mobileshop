# Generated by Django 5.1.2 on 2024-10-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_alter_categories_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='Brand_Image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
