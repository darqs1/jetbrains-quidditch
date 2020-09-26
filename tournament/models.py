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

team_model_manager = Team.objects
player_model_manager = Player.objects
