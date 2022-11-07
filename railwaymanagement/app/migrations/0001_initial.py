# Generated by Django 4.1.3 on 2022-11-07 16:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('from_station', models.CharField(max_length=50)),
                ('to_station', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('STOPPED', 'STOPPED'), ('STARTED', 'STARTED'), ('RUNNING', 'RUNNING'), ('DELAYED', 'DELAYED')], default='STARTED', max_length=50)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('total_seats', models.IntegerField(default=0)),
                ('available_seats', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('booked_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]