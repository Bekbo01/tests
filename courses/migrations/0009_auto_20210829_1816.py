# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-29 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_badgeaward'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='users',
        ),
        migrations.DeleteModel(
            name='Cluster',
        ),
    ]
