# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('hash_name', models.CharField(unique=True, max_length=255, blank=True)),
                ('website', models.ForeignKey(default=None, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to=b'img/logo/')),
                ('background', models.CharField(max_length=9, blank=True)),
                ('background_image', models.ImageField(upload_to=b'img/bg/', blank=True)),
                ('website', models.ForeignKey(default=None, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email address', blank=True)),
                ('ip', models.CharField(default=b'', max_length=255)),
                ('hash_name', models.CharField(unique=True, max_length=255, blank=True)),
                ('opened', models.ManyToManyField(related_name='emails_opened', to='server.Email')),
                ('received', models.ManyToManyField(related_name='emails_received', to='server.Email')),
                ('website', models.ForeignKey(default=None, to='sites.Site')),
            ],
        ),
    ]
