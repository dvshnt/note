# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_emailnote_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='body',
        ),
    ]
