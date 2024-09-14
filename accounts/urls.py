from . import views
from django.urls import path
urlpatterns = [
    path("login/", views.login,name="login"),
    path("signup/", views.signup,name="signup"),
    path("profile_data/<id>/", views.signup,name="profile"),
]
