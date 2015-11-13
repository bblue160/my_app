# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='description',
            new_name='synopsys',
        ),
    ]
