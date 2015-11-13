# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20151109_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='sospi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data', models.IntegerField()),
            ],
        ),
    ]
