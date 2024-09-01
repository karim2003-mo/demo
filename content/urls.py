from django.urls import path
from . import views
urlpatterns = [
    path('teams/',views.all_teams,name="all_teams")
]
