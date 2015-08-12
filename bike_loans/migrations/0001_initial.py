# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(default='UNA', choices=[('AVA', 'Available'), ('BRK', 'Broken'), ('USE', 'In use'), ('UNA', 'Unavailable')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(default='IPG', choices=[('FIN', 'Finished'), ('IPG', 'In progress')], max_length=3)),
                ('duration', models.DurationField()),
                ('data_time', models.DateTimeField()),
                ('bike', models.ForeignKey(to='bike_loans.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('rfid', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(to='bike_loans.User'),
        ),
    ]
