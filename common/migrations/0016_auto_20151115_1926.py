# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_userprofile_compare'),
    ]

    operations = [
        migrations.CreateModel(
            name='compare',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='compare',
        ),
        migrations.AddField(
            model_name='compare',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
