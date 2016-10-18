# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0018_auto_20160922_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='header',
            field=models.BooleanField(default=False, help_text=b'Show logo at top of email?'),
        ),
    ]
