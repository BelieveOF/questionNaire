# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='options',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questionnaires',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='title_id',
            new_name='title',
        ),
    ]
