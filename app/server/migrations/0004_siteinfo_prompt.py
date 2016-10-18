# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20160825_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='prompt',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
