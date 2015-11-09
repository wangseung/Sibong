# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_newslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usermoney',
            field=models.IntegerField(null=True),
        ),
    ]
