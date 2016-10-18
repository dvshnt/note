# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20160901_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnote',
            name='category',
            field=models.IntegerField(default=None, choices=[(b'brief', b'Brief'), (b'beat', b'Beat')]),
        ),
    ]
