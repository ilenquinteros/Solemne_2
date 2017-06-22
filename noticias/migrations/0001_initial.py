# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categoria', models.CharField(max_length=100, unique=True)),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('fecha_creacion_C', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion_C', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_titulo', models.CharField(max_length=100, unique=True)),
                ('titulo_noticia', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/data')),
                ('fecha_creacion_N', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion_N', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.Category')),
            ],
        ),
    ]
