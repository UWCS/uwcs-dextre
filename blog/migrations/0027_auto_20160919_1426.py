# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('blog', '0026_auto_20160917_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ContactIndexPage',
        ),
        migrations.DeleteModel(
            name='ExecPage',
        ),
    ]
