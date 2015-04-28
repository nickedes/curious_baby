# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ansid', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='id',
        ),
        migrations.AddField(
            model_name='choice',
            name='cid',
            field=models.IntegerField(primary_key=True, default=1, serialize=False),
        ),
    ]
