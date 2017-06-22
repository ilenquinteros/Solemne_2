# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from noticias.models import Category, News
from django.http import Http404

def home(request):

	lista_noticias = News.objects.order_by('fecha_creacion')
	
	noticia_destacada = News.objects.filter(destacada=True).latest('fecha_creacion')
	
	return render(request, 'base/index.html', {'lista_noticias':lista_noticias, 'destacada': noticia_destacada})

def category(request,category_id):

    products = Product.objects.filter(category__id=category_id, status=1)

    categories = Category.objects.filter(status=1)

    return render(request, 'category.html', {'products':products, 'categories':categories})


def noticia_detalle(request,id_noticia):
	try:
		id_noticia = int(id_noticia)
	except ValueError:
		raise Http404()
	noticia = News.objects.filter(id_noticia=id_noticia)
	return render(request, 'noticia_detalle.html', {'noticia': noticia})
