# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-06 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_notified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notified',
            name='clicked_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
