from django.shortcuts import render, redirect
from .forms import PlayerForm, DuoForm, TeamForm, UserRegistrationForm
from .models import Player, Duo, Team
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'Valorant-Home.html')


def index(request):
    list = Player.objects.all()
    context = {'list': list}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def duopartner(request, id):
    duo = Duo.objects.get(id=id)
    this_user = request.user
    try:
        player = Player.objects.get(user_name=this_user)
        duo.players_signedup += player.player_name + ', '
        duo.save()
        messages.success(request, 'You successfully signed up to be ' + duo.player_name + "'s partner!")
        return redirect('duoindex')
    except:
        messages.error(request, 'You need to sign up as a player first')
        return redirect('duoindex')


@login_required(login_url='login')
def teampartner(request, id):
    team = Team.objects.get(id=id)
    this_user = request.user
    try:
        player = Team.objects.get(user_name=this_user)
        team.players_signedup += player.player_name + ', '
        team.save()
        messages.success(request, 'You successfully challenged ' + team.team_name)
        return redirect('home')
    except:
        messages.error(request, 'You need to be a captain of a team to challenge')
        return redirect('teamindex')


@login_required(login_url='login')
def duoindex(request):
    this_user = request.user
    list = Duo.objects.all()
    newlist = list.exclude(user_name=this_user)
    context = {'list': newlist}
    return render(request, 'duo-index.html', context)


@login_required(login_url='login')
def teamindex(request):
    this_user = request.user
    list = Team.objects.all()
    newlist = list.exclude(user_name=this_user)
    context = {'list': newlist}
    return render(request, 'team-index.html', context)


@login_required(login_url='login')
def playersign(request):
    this_user = request.user
    list = Player.objects.all()
    if list.filter(user_name=this_user).exists():
        messages.error(request, 'You already signed up')
        return redirect('home')
    else:
        form = PlayerForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                complete_form = form.save(commit=False)
                complete_form.user_name = this_user
                complete_form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'player-sign.html', context)


@login_required(login_url='login')
def duosign(request):
    this_user = request.user
    list = Duo.objects.all()
    if list.filter(user_name=this_user).exists():
        messages.error(request, 'You already signed up')
        return redirect('home')
    else:
        form = DuoForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                complete_form = form.save(commit=False)
                complete_form.user_name = request.user
                complete_form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'duo-sign.html', context)


@login_required(login_url='login')
def teamsign(request):
    form = TeamForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            complete_form = form.save(commit=False)
            complete_form.user_name = request.user
            complete_form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'team-sign.html', context)


def deleteduo(request, id):
    duo = Duo.objects.get(id=id)
    duo.delete()
    messages.success(request, 'You have deleted your duo page')
    return redirect('home')


def deleteteam(request, id):
    team = Team.objects.get(id=id)
    team.delete()
    messages.success(request, "You have deleted your team's page")
    return redirect('home')


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
    try:
        account = Duo.objects.get(user_name=user)
        context = {'account': account}
        return render(request, 'your-duo.html', context)
    except:
        messages.error(request, 'You do not have a duo page, sign up for one with the sign up dropdown menu')
        return redirect('home')


@login_required(login_url='login')
def yourteam(request):
    user = request.user
    try:
        account = Team.objects.get(user_name=user)
        context = {'account': account}
        return render(request, 'your-team.html', context)
    except:
        messages.error(request,
                       'You do not have a team page or are not the captain, sign up for one with the sign up dropdown menu')
        return redirect('home')
