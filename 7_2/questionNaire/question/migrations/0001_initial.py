# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]