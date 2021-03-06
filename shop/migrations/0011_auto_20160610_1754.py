# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_carousel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name_plural': 'Carousel'},
        ),
        migrations.AddField(
            model_name='carousel',
            name='name',
            field=models.CharField(default=b'carousel', max_length=25),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'category/carousel-images/'),
        ),
    ]
