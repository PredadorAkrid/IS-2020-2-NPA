from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from music.forms import *
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout


##Class-based-views
class Index(View):
    def get(self, request):
        return render(request, 'music/index.html')
    def post(self, request):
        return HttpResponseForbidden()

class TopSongs(View):
	def get(self, request):
		songs = Song.objects.all()
		to_play_id = request.GET.get("to_play", 1)
		songs_to_play = Song.objects.filter(id_song=to_play_id)
		if songs_to_play.count() == 0:
			to_play = Song.objects.first()
		else:
			to_play = songs_to_play.first()
		context = {"songs": songs, "to_play": to_play}
		return render(request,'music/top_songs.html', context)
class AddArtist(View):
    def get(self, request):
        form = AddArtistForm()
        context = {"form": form}
        return render(request, 'music/create_artist.html', context)  
    def post(self, request):
        form = AddArtistForm(request.POST, request.FILES)
        print(form)
        if not form.is_valid():
            context = {"form": form}
            return render(request, 'music/create_artist.html', context)
            
        Artist.objects.create(
            id_artist=form.cleaned_data["artist"],
            name=form.cleaned_data["name"],
            image=form.cleaned_data["image"],
            
        )
        return HttpResponse("<h1>Artist Created!</h1>")