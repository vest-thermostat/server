# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 20:18
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJourney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userlocation',
            options={'get_latest_by': 'created'},
        ),
        migrations.AddField(
            model_name='userjourney',
            name='finish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finish_location', to='location.UserLocation'),
        ),
        migrations.AddField(
            model_name='userjourney',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userjourney',
            name='start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_location', to='location.UserLocation'),
        ),
    ]
