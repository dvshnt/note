# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0017_auto_20160920_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(default=b'A hero or a villain writing for The Nashville Note.', help_text=b'Brief bio about author.'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='background',
            field=models.CharField(help_text=b'Background color as HEX value.', max_length=9, verbose_name=b'Background Color', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='background_image',
            field=models.ImageField(help_text=b'Background image to be repeated as a tile.', upload_to=server.models.get_upload_path_bg, verbose_name=b'Background Image', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='description',
            field=models.TextField(help_text=b'Description of site. Shown on signup splash pages.', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='email',
            field=models.EmailField(help_text=b'Publicly displayed contact email.', max_length=254),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='facebook',
            field=models.URLField(verbose_name=b'Facebook URL', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='gatracking',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'GA Tracking Code'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='instagram',
            field=models.URLField(verbose_name=b'Instagram URL', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='logo',
            field=models.ImageField(upload_to=server.models.get_upload_path_logo),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='name',
            field=models.CharField(help_text=b"Name of site to be used as page's title, og:title and anywhere the title is requested.", max_length=255),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='ogdescription',
            field=models.CharField(default=b'', help_text=b'Description to be displayed in OG crawls.', max_length=512, verbose_name=b'OG Description'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='ogimg',
            field=models.ImageField(default=b'', help_text=b'Image to be used for Open Graph crawls. Dimensions: 1200px x 630px', verbose_name=b'OG Image', upload_to=server.models.get_upload_path_og),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='ogtitle',
            field=models.CharField(default=b'', help_text=b'Title to be displayed in OG crawls.', max_length=255, verbose_name=b'OG Title'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='prompt',
            field=models.CharField(default=b'', help_text=b'Text to be shown above email signup form.', max_length=500, verbose_name=b'Signup Prompt'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='twitter',
            field=models.URLField(verbose_name=b'Twitter URL', blank=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='youtube',
            field=models.URLField(verbose_name=b'YouTube URL', blank=True),
        ),
    ]
