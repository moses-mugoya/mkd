# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170920_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='songFile',
            field=models.FileField(upload_to='mysongs'),
        ),
    ]