# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20160901_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(null=True, upload_to='upload_files/competitions/images'),
        ),
    ]