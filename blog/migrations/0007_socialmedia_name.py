# Generated by Django 3.0.8 on 2020-07-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
