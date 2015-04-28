# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0005_auto_20150428_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='qid',
            field=models.ForeignKey(default=0, to='ques.questions'),
        ),
    ]
