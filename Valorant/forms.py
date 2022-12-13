from django import forms
from .models import Player, Duo, Team
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

RANKS = (
    ('IRON I', 'IRON1'),
    ('IRON II', 'IRON2'),
    ('IRON III', 'IRON3'),
    ('BRONZE I', 'BRONZE1'),
    ('BRONZE II', 'BRONZE2'),
    ('BRONZE III', 'BRONZE3'),
    ('SILVER I', 'SILVER1'),
    ('SILVER II', 'SILVER2'),
    ('SILVER III', 'SILVER3'),
    ('GOLD I', 'GOLD1'),
    ('GOLD II', 'GOLD2'),
    ('GOLD III', 'GOLD3'),
    ('PLATINUM I', 'PLATINUM1'),
    ('PLATINUM II', 'PLATINUM2'),
    ('PLATINUM III', 'PLATINUM3'),
    ('DIAMOND I', 'DIAMOND1'),
    ('DIAMOND II', 'DIAMOND2'),
    ('DIAMOND III', 'DIAMOND3'),
    ('ASCENDANT I', 'ASCENDANT1'),
    ('ASCENDANT II', 'ASCENDANT2'),
    ('ASCENDANT III', 'ASCENDANT3'),
    ('IMMORTAL I', 'IMMORTAL1'),
    ('IMMORTAL II', 'IMMORTAL2'),
    ('IMMORTAL III', 'IMMORTAL3'),
    ('RADIANT', 'RADIANT')
)
AGENTS = (
    ('No main', 'NONE'),
    ('Brimstone', 'Brimstone'),
    ('Pheonix', 'Pheonix'),
    ('Sage', 'Sage'),
    ('Sova', 'Sova'),
    ('Viper', 'Viper'),
    ('Cypher', 'Cypher'),
    ('Reyna', 'Reyna'),
    ('Killjoy', 'Killjoy'),
    ('Breach', 'Breach'),
    ('Omen', 'Omen'),
    ('Jett', 'Jett'),
    ('Raze', 'Raze'),
    ('Skye', 'Skye'),
    ('Yoru', 'Yoru'),
    ('Astra', 'Astra'),
    ('Kayo', 'Kayo'),
    ('Chamber', 'Chamber'),
    ('Neon', 'Neon'),
    ('Fade', 'Fade'),
    ('Harbor', 'Harbor')
)


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('player_name', 'player_rank',)
        player_name = forms.CharField(max_length=30)
        player_rank = forms.ChoiceField(choices=RANKS)

        widgets = {
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your valorant name'}),
            'player_rank': forms.RadioSelect(choices=RANKS, attrs={'id': 'value'})
        }


class DuoForm(forms.ModelForm):
    class Meta:
        model = Duo
        fields = ('player_name', 'player_rank', 'main_agents',)
        player_name = forms.CharField(max_length=30)
        player_rank = forms.ChoiceField(choices=RANKS)
        main_agents = forms.MultipleChoiceField(choices=AGENTS)

        widgets = {
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your valorant name'}),
            'player_rank': forms.RadioSelect(choices=RANKS, attrs={'id': 'value'}),
            'main_agents': forms.CheckboxSelectMultiple(choices=AGENTS)
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'player_name', 'player_rank')
        team_name = forms.CharField(max_length=30)
        player_name = forms.CharField(max_length=30)
        player_rank = forms.ChoiceField(choices=RANKS)

        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Team name'}),
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your captain's name name"}),
            'player_rank': forms.RadioSelect(choices=RANKS, attrs={'id': 'value'})
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'})
        }
