# Generated by Django 3.2.15 on 2022-10-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0020_alter_eventpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventsignup",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="eventtype",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
