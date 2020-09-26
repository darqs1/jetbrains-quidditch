from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=64)

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

# team_model_manager = Team.objects
# player_model_manager = Player.objects
#
# falmouth_falcons = Team.objects.create(name="Falmouth Falcons")
# montrose_magpies = Team.objects.create(name="Montrose Magpies")
#
# Player.objects.create(name="Karl Broadmoor", height=180, team=falmouth_falcons)
# Player.objects.create(name="Kevin Broadmoor", height=183, team=falmouth_falcons)
# Player.objects.create(name="Alasdair Maddock", height=175, team=montrose_magpies)
# Player.objects.create(name="Lennox Campbell", height=197, team=montrose_magpies)
