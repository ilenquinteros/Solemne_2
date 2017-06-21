# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField
from django.db import models

class Category(models.Model):
	id_categoria = models.CharField(max_length=100, unique=True)
    nombre_categoria = models.TextField()
    fecha_creacion_C = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_C = models.DateTimeField(auto_now=True)
    # sort_order = models.IntegerField(default=0)
    # status = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class News(models.Model):
    id_titulo = models.CharField(max_length=100,unique=True)
    titulo_noticia = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Category, null=True)
    imagen = models.ImageField(upload_to='images/data',blank=True,null=True)
    fecha_creacion_N = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_N = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku
