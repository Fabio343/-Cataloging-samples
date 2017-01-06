# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-06 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sedimentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ambiente',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='coletador',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='data',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='descrição',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='amostra',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='geologia',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='clima',
            name='tipo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='continente',
            name='nome',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='continente',
            name='sigla',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='país',
            name='nome',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='país',
            name='região',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
