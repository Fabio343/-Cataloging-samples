# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sedimentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coletador',
            name='come',
        ),
        migrations.AddField(
            model_name='coletador',
            name='nome',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amostra',
            name='ambiente',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='descrição',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='tipo',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='geologia',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='clima',
            name='tipo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='coletador',
            name='país',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.país'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='país',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='país',
            name='região',
            field=models.CharField(max_length=20),
        ),
    ]
