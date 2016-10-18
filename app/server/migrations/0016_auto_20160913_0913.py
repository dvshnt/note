# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_email_introimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='ogdescription',
            field=models.CharField(default=b'', max_length=512),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='ogimg',
            field=models.ImageField(default=b'', upload_to=b'img/logo/'),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='ogtitle',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='email',
            name='introimg',
            field=models.ImageField(default=None, upload_to=b'img/covers/'),
        ),
    ]
