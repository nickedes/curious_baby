# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0003_auto_20150428_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='cid',
            field=models.IntegerField(primary_key=True, serialize=False, default=1),
        ),
    ]
