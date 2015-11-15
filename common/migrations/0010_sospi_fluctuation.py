# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20151114_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='sospi',
            name='fluctuation',
            field=models.IntegerField(default=0),
        ),
    ]
