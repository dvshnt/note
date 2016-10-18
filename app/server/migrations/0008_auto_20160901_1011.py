# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_remove_email_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='opened',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='received',
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='opened_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
