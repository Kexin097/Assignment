from django.urls import path
from . import views

urlpatterns = [
    path("", views.world, name='world'),
    path("asia", views.asia, name="asia"),
    path("malaysia", views.malaysia, name='malaysia')
]