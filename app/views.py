from django.http import HttpResponse
from django.shortcuts import render

# from django.shotcuts import render
def create(request):
    return render(request, 'create.html', {'form': form})

def client_create(request):

	

	return HttpResponse("<h1>create<h1/>")


def detail(request):
    return HttpResponse("<h1>detail<h1/>")

def list(request):
    return HttpResponse("<h1>list<h1/>")

def update(request):
    return HttpResponse("<h1>update<h1/>")

def delete(request):
    return HttpResponse("<h1>delete<h1/>")


