# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20151115_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='compare',
            field=models.IntegerField(default=0),
        ),
    ]
