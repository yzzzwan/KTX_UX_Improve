# Generated by Django 4.2.16 on 2024-11-30 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_schedules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainschedule',
            old_name='train',
            new_name='train_id',
        ),
    ]
