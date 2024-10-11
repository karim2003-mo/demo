from . import views
from . import manage_accounts
from django.urls import path
urlpatterns = [
    path("login/", views.login,name="login"),
    path("signup/", views.signup,name="signup"),
    path("profile_data/<id>/", views.profile_data,name="profile"),
    path("postplayer/", views.postplayer,name="postplayer"),
    path("postsubs/", views.substitution,name="substitution"),
    path("post_players_point/<str:type>/", views.post_players_point,name="substitution"),
    path("add_score/<str:type>/", views.update_users_score,name="add_score"),
    path("done/<str:receiver_email>", manage_accounts.verification_done,name="done"),
]
