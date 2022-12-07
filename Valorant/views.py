from django.shortcuts import render, redirect
from .forms import PlayerForm, DuoForm, UserRegistrationForm
from .models import Player, Duo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Valorant-Home.html')


def index(request):
    list = Player.objects.all()
    context = {'list': list}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def duoindex(request):
    list = Duo.objects.all()
    context = {'list': list}
    return render(request, 'duo-index.html', context)


@login_required(login_url='login')
def playersign(request):
    form = PlayerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            complete_form = form.save(commit=False)
            complete_form.user_name = request.user
            complete_form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'player-sign.html', context)


@login_required(login_url='login')
def duosign(request):
    form = DuoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            complete_form = form.save(commit=False)
            complete_form.user_name = request.user
            complete_form.save()
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


@login_required(login_url='login')
def userindex(request):
    return render(request, 'userindex.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def yourduo(request):
    user = request.user
    account = Duo.objects.get(user_name=user)
    context = {'account': account}
    return render(request, 'your-duo.html', context)
