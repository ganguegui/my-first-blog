# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-29 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_aluno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='id',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
