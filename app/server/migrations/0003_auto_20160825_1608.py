# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20160825_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='sent_at',
            field=models.DateTimeField(default=None, blank=True),
        ),
    ]
