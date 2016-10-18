# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_email_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailnote',
            name='blurb',
        ),
        migrations.RemoveField(
            model_name='emailnote',
            name='image',
        ),
        migrations.RemoveField(
            model_name='emailnote',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='emailnote',
            name='title',
        ),
        migrations.AddField(
            model_name='emailnote',
            name='content',
            field=tinymce.models.HTMLField(default=b''),
        ),
    ]
