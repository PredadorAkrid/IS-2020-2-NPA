from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from .models import *


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
