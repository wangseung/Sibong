# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20151106_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='havestock',
            old_name='mystock',
            new_name='stockitem',
        ),
        migrations.AlterField(
            model_name='havestock',
            name='count',
            field=models.SmallIntegerField(default=0),
        ),
    ]
