# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('server', '0004_siteinfo_prompt'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_at', models.DateTimeField()),
                ('opened_at', models.DateTimeField(blank=True)),
                ('stats', jsonfield.fields.JSONField(default=dict, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('blurb', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='email',
            name='sent_at',
        ),
        migrations.AddField(
            model_name='emailnote',
            name='email',
            field=models.ForeignKey(to='server.Email'),
        ),
        migrations.AddField(
            model_name='emailnote',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='emaillog',
            name='email',
            field=models.ForeignKey(to='server.Email'),
        ),
        migrations.AddField(
            model_name='emaillog',
            name='subscriber',
            field=models.ForeignKey(to='server.Subscriber'),
        ),
    ]
