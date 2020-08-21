# Generated by Django 3.0.8 on 2020-07-25 20:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200720_2245'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatingrevision',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='seatingrevision',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='seatingrevision',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='has_seating',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='seating_location',
        ),
        migrations.AddField(
            model_name='eventpage',
            name='signup_type',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Internal'), (2, 'External')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventpage',
            name='signup_url',
            field=models.URLField(blank=True, help_text='External only'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_close',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Internal only'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_freshers_open',
            field=models.DateTimeField(blank=True, help_text='Set a date for when freshers may sign up to the event, leave blank if they are to sign up at the same time as everyone else. Internal only', null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_limit',
            field=models.IntegerField(default=0, help_text='Enter 0 for unlimited signups. Internal only', verbose_name='Signup limit'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_open',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Internal only'),
        ),
        migrations.DeleteModel(
            name='Seating',
        ),
        migrations.DeleteModel(
            name='SeatingRevision',
        ),
        migrations.DeleteModel(
            name='SeatingRoom',
        ),
    ]