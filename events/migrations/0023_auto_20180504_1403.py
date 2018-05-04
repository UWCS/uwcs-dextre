# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-04 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20180319_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='has_seating',
            field=models.BooleanField(default=False, help_text='Tick this if the event needs a seating plan'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='seating_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.SeatingRoom'),
        ),
        migrations.AlterField(
            model_name='seatingroom',
            name='tables_raw',
            field=models.TextField(help_text='This field will contain a literal array of integers in JSON list notation ([2, 3, 4, 5]). Each position corresponds to a table, and the value is the total seats on that table. For example: [20, 20, 20, 10] would be the standard LIB2 set up.'),
        ),
    ]
