# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='havestock',
            name='count',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='havestock',
            name='mystock',
            field=models.ForeignKey(to='common.Stock'),
        ),
    ]
