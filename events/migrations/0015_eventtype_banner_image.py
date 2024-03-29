# Generated by Django 3.1 on 2020-09-15 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("events", "0014_auto_20200914_2136"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventtype",
            name="banner_image",
            field=models.ForeignKey(
                blank=True,
                help_text="This image will be displayed as the event page banner",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
