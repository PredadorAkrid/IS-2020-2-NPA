from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        print("entra a index post")
        return HttpResponseForbidden()
