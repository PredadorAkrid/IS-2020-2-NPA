from django.urls import path
from django.conf.urls import url,include
from music import views

app_name = "music"

urlpatterns = [
    ##Ésto lo haríamos si usáramos funciones como vistas
    #path('',index),
    #path('top_songs', songs),
   	##Ésto lo haríamos si usáramos clases como vistas
   	

   	path("", views.Index.as_view(), name="Index"),
    path("top-songs", views.TopSongs.as_view(), name="top-songs"),
    path("artist/create-artist", views.AddArtist.as_view(), name="add_artist"),

]