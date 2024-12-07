from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Buyer, Game
def index(request):
    return render(request, 'index.html')
def games_list(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})
def cart(request):
    return render(request, 'cart.html')
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not Buyer.objects.filter(name=username).exists():
            Buyer.objects.create(name=username, balance=0.0, age=18)
            return redirect('index')
    return render(request, 'registration.html')
