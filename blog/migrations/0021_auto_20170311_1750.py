# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170311_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_counter',
            field=models.PositiveIntegerField(default=10),
        ),
    ]