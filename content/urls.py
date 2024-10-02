from django.urls import path
from . import views
from . import views2
urlpatterns = [
    path('teams/',views.all_teams,name="all_teams"),
    path("<team>/players/",views.view_player,name="palyers"),
    path("players/Gk/",views.Gk,name="Gk"),
    path("players/Cb/",views.Cb,name="Gk"),
    path("players/Cmf/",views.Cmf,name="Gk"),
    path("players/Cf/",views.Cf,name="Gk"),
    path("players/getsquad/",views.getsquad,name="getsquad"),
    path("grep_events/",views.made_json_teams,name="grep_events"),
    path("get_public_info/",views.get_public_info,name="get_public_info"),
    path("player_points/<str:team>/<str:type>/",views.player_points,name="player_points"),
    path("post_players_point/",views2.post_players_point,name="post_players_point"),
]
