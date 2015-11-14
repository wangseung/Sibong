# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_sospi_fluctuation'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockprice',
            name='fluctuation',
            field=models.IntegerField(default=0),
        ),
    ]
