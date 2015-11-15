# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20151113_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='sospi',
            name='today',
            field=models.IntegerField(default=14),
            preserve_default=False,
        ),
    ]
