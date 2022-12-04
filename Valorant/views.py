from django.shortcuts import render, redirect
from .forms import PlayerForm, DuoForm
from .models import Player, Duo


def home(request):
    return render(request, 'Valorant-Home.html')


def index(request):
    list = Player.objects.all()
    context = {'list': list}
    return render(request, 'index.html', context)


def duoindex(request):
    list = Duo.objects.all()
    context = {'list': list}
    return render(request, 'duo-index.html', context)


def playersign(request):
    form = PlayerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'player-sign.html', context)


def duosign(request):
    form = DuoForm(request.POST or None)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'duo-sign.html', context)


def deleteduo(request, id):
    duo = Duo.objects.get(id=id)
    duo.delete()
    return redirect('duoindex')


def deleteplayer(request, id):
    player = Player.objects.get(id=id)
    player.delete()
    return redirect('index')
