# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151117_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
        migrations.AddField(
            model_name='review',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
    ]
