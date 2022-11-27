from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index/index.html") 

def login(request):
    return render(request, "index/login.html")

def cadastre(request):
    return render(request, "index/cadastre.html")

def produtos(request):
    return render(request, "index/produtos.html")
 

