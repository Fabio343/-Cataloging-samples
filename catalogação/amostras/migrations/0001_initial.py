# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-14 13:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, unique=True)),
                ('tipo', models.CharField(blank=True, max_length=25, null=True)),
                ('descrição', models.TextField(blank=True, max_length=300, null=True)),
                ('data', models.CharField(blank=True, max_length=15, null=True)),
                ('granulometria', models.FileField(blank=True, null=True, upload_to='')),
                ('coletador', models.CharField(blank=True, max_length=50, null=True)),
                ('imagem', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem1', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem2', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem3', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem4', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem5', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem6', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem7', models.FileField(blank=True, null=True, upload_to='')),
                ('imagem8', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=55, null=True)),
                ('geologia', models.TextField(blank=True, max_length=300, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra')),
            ],
        ),
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=40, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('sigla', models.CharField(max_length=10)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=55, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra')),
                ('continente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Continente')),
            ],
        ),
        migrations.CreateModel(
            name='País',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35)),
                ('região', models.CharField(blank=True, max_length=75, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra')),
                ('continente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Continente')),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='país',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.País'),
        ),
        migrations.AddField(
            model_name='clima',
            name='continente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Continente'),
        ),
        migrations.AddField(
            model_name='clima',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Estado'),
        ),
        migrations.AddField(
            model_name='clima',
            name='país',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.País'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='continente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Continente'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Estado'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='país',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.País'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostras.Amostra'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Cidade'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='continente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Continente'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.Estado'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='país',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amostras.País'),
        ),
    ]
