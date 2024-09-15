from django.urls import path
from . import views
urlpatterns = [
    path('teams/',views.all_teams,name="all_teams"),
    path("<team>/players/",views.view_player,name="palyers"),
    path("players/Gk/",views.Gk,name="Gk"),
    path("players/Cb/",views.Cb,name="Gk"),
    path("players/Cmf/",views.Cmf,name="Gk"),
    path("players/Cf/",views.Cf,name="Gk"),
]
