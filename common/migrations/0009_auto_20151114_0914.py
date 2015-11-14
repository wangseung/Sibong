# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_sospi_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sospi',
            name='today',
        ),
        migrations.AddField(
            model_name='sospi',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sospi',
            name='month',
            field=models.IntegerField(default=0),
        ),
    ]
