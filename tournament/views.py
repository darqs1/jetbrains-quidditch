from django.shortcuts import render
from django.views import View
from tournament.models import Team, Player
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

class TournamentViews(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all
        return render(request, 'tournament/tournament.html', context={'players': players})

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'tournament/signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'tournament/login.html'

