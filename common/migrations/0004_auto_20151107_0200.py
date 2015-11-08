# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20151107_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usermoney',
            field=models.IntegerField(default=10000000),
        ),
    ]
