from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("asia", views.asia, name="asia"),
    path("malaysia", views.malaysia, name='malaysia')
]