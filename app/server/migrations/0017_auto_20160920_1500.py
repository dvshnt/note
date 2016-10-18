# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_auto_20160913_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnote',
            name='subtitle',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='gatracking',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='email',
            name='introimg',
            field=models.ImageField(default=None, upload_to=b'img/covers/', blank=True),
        ),
        migrations.AlterField(
            model_name='emailnote',
            name='category',
            field=models.IntegerField(choices=[(1, b'Intro'), (2, b'Brief'), (3, b'Beat'), (4, b'Poster'), (5, b'Quote')]),
        ),
    ]
