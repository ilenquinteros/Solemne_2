# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin
from noticias.models import Category, News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','nombre_categoria', 'fecha_creacion','fecha_modificacion')
    #list_filter = ('owner','active')
    search_fields = ('nombre_categoria',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id_noticia','titulo_noticia','categoria','fecha_creacion', 'destacada')
    search_fields = ('titulo_noticia',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)