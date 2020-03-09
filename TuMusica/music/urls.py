from django.urls import path
from django.conf.urls import url,include
from music import views


urlpatterns = [
    ##Ésto lo haríamos si usáramos funciones como vistas
    #path('',index),
    #path('top_songs', songs),
   	##Ésto lo haríamos si usáramos clases como vistas
   	path('', views.Index.as_view(), name='Index'),
   	path('top_songs', views.Songs.as_view(), name='Songs'),
]