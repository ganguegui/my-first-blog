from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Bem Vindo ao Blog!!")

def index(request):
    return render(request,'index.html')

def exibir(request):
    return render(request,'perfil.html')
