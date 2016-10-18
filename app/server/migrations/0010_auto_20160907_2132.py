# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20160907_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('img', models.ImageField(upload_to=b'img/profile/')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('contact_email', models.EmailField(default=None, max_length=254)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='email',
            field=models.ForeignKey(to='server.Email', blank=True),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='subscriber',
            field=models.ForeignKey(to='server.Subscriber', blank=True),
        ),
        migrations.AlterField(
            model_name='emailnote',
            name='category',
            field=models.IntegerField(choices=[(1, b'Intro'), (2, b'Brief'), (3, b'Beat'), (4, b'Poster')]),
        ),
    ]
