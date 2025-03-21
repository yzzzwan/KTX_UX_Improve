# Generated by Django 4.2.16 on 2024-11-30 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train_schedules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myticket',
            name='schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='train_schedules.trainschedule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myticket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
