# Generated by Django 3.1 on 2020-09-14 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('events', '0013_auto_20200821_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='list_image',
            field=models.ForeignKey(blank=True,
                                    help_text='This image will be displayed beside the event on the front page and event list',
                                    null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to='wagtailimages.image'),
        ),
    ]