# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userinfo_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
