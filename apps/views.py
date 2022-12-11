from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, "index/index.html") 

def cadastre(request):
    if request.method=='GET':     
        return render(request, "index/cadastre.html")
    elif request.method=='POST':
        content = request.POST
        user = User.objects.create_user(username=content.get('username'),
                                        email=content.get('email'),
                                        password=content.get('password'))
        print(request.POST)
        
        return redirect('home')
@login_required
def produtos(request):
    return render(request, "index/produtos.html")

@login_required
def carrinho(request):
    return render(request,"index/carrinho.html")
