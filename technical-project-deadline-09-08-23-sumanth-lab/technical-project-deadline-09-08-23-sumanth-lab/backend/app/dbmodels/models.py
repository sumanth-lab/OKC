# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

# done
class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    homeTeam = models.OneToOneField(
        'Team',
        on_delete=models.CASCADE,
        related_name='home_team',
    )
    awayTeam = models.OneToOneField(
        'Team',
        on_delete=models.CASCADE,
        related_name='home_team',
    )

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    players = models.ManyToManyField(
        'Player',
        through='GamePlayer',
    )

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    is_starter = models.BooleanField()
    minutes = models.IntegerField(primary_key=False)
    points = models.IntegerField(primary_key=False)
    assists = models.IntegerField(primary_key=False)
    offensiveRebounds = models.IntegerField(primary_key=False)
    defensiveRebounds = models.IntegerField(primary_key=False)
    steals = models.IntegerField(primary_key=False)
    blocks = models.IntegerField(primary_key=False)
    turnovers = models.IntegerField(primary_key=False)
    defensiveFouls = models.IntegerField(primary_key=False)
    offensiveFouls = models.IntegerField(primary_key=False)
    freeThrowsMade = models.IntegerField(primary_key=False)
    freeThrowsAttempted = models.IntegerField(primary_key=False)
    twoPointersMade = models.IntegerField(primary_key=False)
    twoPointersAttempted = models.IntegerField(primary_key=False)
    threePointersMade = models.IntegerField(primary_key=False)
    threePointersAttempted = models.IntegerField(primary_key=False)
    shots = models.ManyToManyField(
        'Shot',
        through='GameShot',
    )

class Shot(models.Model):
    is_make = models.BooleanField()
    locationX = models.DecimalField(max_digits=5, decimal_places=1)
    locationY = models.DecimalField(max_digits=5, decimal_places=1)



# done
class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
# done
class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

