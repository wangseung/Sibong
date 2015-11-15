# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_auto_20151115_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='havestock',
            old_name='mystock',
            new_name='my_stock',
        ),
    ]
