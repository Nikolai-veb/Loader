# Generated by Django 3.1.4 on 2020-12-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_images_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
