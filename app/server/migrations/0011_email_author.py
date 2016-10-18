# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20160907_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='author',
            field=models.ForeignKey(default=1, to='server.Author'),
        ),
    ]
