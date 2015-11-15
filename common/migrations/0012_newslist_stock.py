# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_stockprice_fluctuation'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslist',
            name='stock',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
