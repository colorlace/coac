# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PieceMove',
        ),
        migrations.AddField(
            model_name='boardstate',
            name='active_color',
            field=models.CharField(default='w', max_length=1),
            preserve_default=False,
        ),
    ]
