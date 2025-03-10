# Generated by Django 4.2.16 on 2024-12-01 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train_schedules', '0002_rename_train_trainschedule_train_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_num', models.PositiveIntegerField()),
                ('schedule_id', models.ForeignKey(db_column='schedule_id', on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='train_schedules.trainschedule')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_num', models.CharField(max_length=10)),
                ('seat_status', models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved')], default='Available', max_length=20)),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='seat.room')),
            ],
            options={
                'verbose_name': 'Seat',
                'verbose_name_plural': 'Seats',
                'db_table': 'seat',
            },
        ),
    ]
