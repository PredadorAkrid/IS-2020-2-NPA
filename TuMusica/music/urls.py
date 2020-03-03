from django.urls import path
from django.conf.urls import url,include
from music.views import *
urlpatterns = [
    path('',index),
    path('top_songs', songs),
]