# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_auto_20160911_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailnote',
            name='content',
        ),
    ]
