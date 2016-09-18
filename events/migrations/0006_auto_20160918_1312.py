# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 13:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160917_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 18, 14, 12, 33, 490888)),
        ),
        migrations.AlterField(
            model_name='eventsignup',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventPage'),
        ),
        migrations.AlterField(
            model_name='eventsignup',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
