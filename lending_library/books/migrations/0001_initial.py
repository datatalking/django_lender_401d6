# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
