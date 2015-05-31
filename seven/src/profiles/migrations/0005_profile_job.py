# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default=b'Janitor', max_length=120),
            preserve_default=True,
        ),
    ]
