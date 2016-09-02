# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20160901_0641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['uploadDate']},
        ),
        migrations.AlterField(
            model_name='video',
            name='converted_video',
            field=models.FileField(blank=True, null=True, upload_to='upload_files/competitions/videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='original_video',
            field=models.FileField(null=True, upload_to='upload_files/competitions/videos'),
        ),
    ]
