# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20151115_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compare',
            old_name='money',
            new_name='compare',
        ),
    ]
