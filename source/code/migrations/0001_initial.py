# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 01:00
from __future__ import unicode_literals

import caching.base
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_live', models.BooleanField(default=True, verbose_name='Display on site')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active project')),
                ('seeking_contributors', models.BooleanField(default=False, verbose_name='Seeking contributors')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('summary', models.TextField(blank=True, help_text='Short, one- or two-sentence version of description, used on list pages.')),
                ('screenshot', sorl.thumbnail.fields.ImageField(blank=True, help_text='Resized to fit 350x250 box in template', null=True, upload_to='img/uploads/code_screenshots')),
                ('repo_last_push', models.DateTimeField(blank=True, null=True)),
                ('repo_forks', models.PositiveIntegerField(blank=True, null=True)),
                ('repo_watchers', models.PositiveIntegerField(blank=True, null=True)),
                ('repo_master_branch', models.CharField(blank=True, max_length=64)),
                ('repo_description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('slug',),
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CodeLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code.Code')),
            ],
            options={
                'verbose_name': 'Code Link',
                'ordering': ('code', 'name'),
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]
