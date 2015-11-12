# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20151110_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('StockPrice', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='StockPrice',
        ),
        migrations.AddField(
            model_name='stockprice',
            name='StockItem',
            field=models.ForeignKey(to='common.Stock'),
        ),
    ]
