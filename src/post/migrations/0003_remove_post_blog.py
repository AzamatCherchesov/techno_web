# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
    ]
