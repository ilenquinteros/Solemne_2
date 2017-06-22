from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^noticia/id/(\d{1,2})/$', views.noticia_detalle),
    # url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    # url(r'^noticia/(?P<product_id>\d+)/$', views.product, name='news'),
]