from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views



##Class-based-views
class Index(View):
    def get(self, request):
        return render(request, 'music/index.html')
    def post(self, request):
        return HttpResponseForbidden()
class Songs(View):
    def get(self, request):
        return render(request,'music/top_songs.html')
    def post(self, request):
        return HttpResponseForbidden()

