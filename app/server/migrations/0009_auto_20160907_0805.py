# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20160901_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnote',
            name='image',
            field=models.ImageField(default=None, upload_to=b'img/poster/', blank=True),
        ),
        migrations.AlterField(
            model_name='emailnote',
            name='category',
            field=models.IntegerField(choices=[(1, b'Brief'), (2, b'Beat'), (3, b'Poster')]),
        ),
    ]
