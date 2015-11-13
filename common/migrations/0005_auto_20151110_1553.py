# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_sospi'),
    ]

    operations = [
        migrations.AddField(
            model_name='havestock',
            name='buy_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='old_usermoney',
            field=models.IntegerField(default=10000000),
        ),
    ]
