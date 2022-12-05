from django.db import models

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


class Player(models.Model):
    player_name = models.CharField(max_length=30)
    player_rank = models.CharField(max_length=30, choices=RANKS, blank=False, default='Unspecified')


class Duo(models.Model):
    player_name = models.CharField(max_length=30)
    player_rank = models.CharField(max_length=30, choices=RANKS, blank=False, default='Unspecified')
    main_agents = models.CharField(max_length=300)
    players_signedup = models.CharField(max_length=1000, blank=True)
