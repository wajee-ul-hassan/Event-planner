# Generated by Django 5.0.3 on 2024-03-13 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_events_venue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]