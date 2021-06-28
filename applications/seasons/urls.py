from django.urls import path
from . import views

app_name = "seasons"

urlpatterns = [
    path('date', views.DateToSeasonsView.as_view(), name= "date"),
    path('seasons', views.GetSeasons.as_view(), name= "seasons"),
]