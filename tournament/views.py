from django.shortcuts import render
from django.views import View
from tournament.models import Team, Player

# Create your views here.

class TournamentViews(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all
        return render(request, 'tournament/tournament.html', context={'players': players})
