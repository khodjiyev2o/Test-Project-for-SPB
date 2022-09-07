from multiprocessing.util import sub_warning
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=54, default="",unique=True)
    email = models.EmailField(max_length=54,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Game(models.Model):
    name = models.CharField(max_length=254, default="")
    players = models.ManyToManyField(Player, blank=True, related_name='player_games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def players_list(self):
        return ",".join([p.name for p in self.players.all()])

    def players_count(self):
        return self.players.count()