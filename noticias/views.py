# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from noticias.models import Category, News
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404

def home(request):
	noticia_destacada = News.objects.filter(destacada=True).latest('fecha_creacion')
	
	lista_noticias = News.objects.filter(~Q(id_noticia = noticia_destacada.id_noticia)).order_by('-fecha_creacion')
	
	return render(request, 'base/index.html', {'lista_noticias':lista_noticias, 'destacada': noticia_destacada})


def noticia_detalle(request,id_noticia):
	try:
		noticia = News.objects.get(id_noticia=id_noticia)
		return render(request, 'noticia_detalle.html', {'noticia': noticia})
	except ObjectDoesNotExist:
		raise Http404()
