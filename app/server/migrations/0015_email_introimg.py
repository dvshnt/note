# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_emailnote_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='introimg',
            field=models.ImageField(default='', upload_to=b'img/covers/'),
            preserve_default=False,
        ),
    ]
