from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("update-score/", views.update_score),
    path("ranking/", views.ranking),
]