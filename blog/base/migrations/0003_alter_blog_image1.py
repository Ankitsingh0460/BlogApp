# Generated by Django 4.1 on 2022-11-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_blog_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image1',
            field=models.ImageField(upload_to='featured_image/'),
        ),
    ]
