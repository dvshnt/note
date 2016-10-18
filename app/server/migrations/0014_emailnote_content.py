# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_remove_emailnote_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnote',
            name='content',
            field=tinymce.models.HTMLField(default=None),
        ),
    ]
