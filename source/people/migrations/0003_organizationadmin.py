# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-17 19:04
from __future__ import unicode_literals

import caching.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Organization')),
            ],
            options={
                'ordering': ('organization', 'email'),
                'verbose_name': 'Organization Admin',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]
