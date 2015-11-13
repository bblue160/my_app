# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151112_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='synopsys',
            new_name='synopsis',
        ),
    ]
