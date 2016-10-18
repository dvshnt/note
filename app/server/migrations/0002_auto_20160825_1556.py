# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='is_test',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='email',
            name='created_at',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='email',
            name='hash_name',
            field=models.CharField(unique=True, max_length=255, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='updated_at',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='hash_name',
            field=models.CharField(unique=True, max_length=255, editable=False, blank=True),
        ),
    ]
