from django.contrib import admin
from .models import Player,Game

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'email')


class PlayersInline(admin.TabularInline):
    model = Game.players.through
    max_num = 5


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'players_list', 'created_at', 'updated_at')
    fields = ('name',)
    inlines = (PlayersInline,)
    
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)