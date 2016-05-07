# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_long_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'category/images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
