from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('postdojo', views.dojo),
    path('postninja', views.ninja),
]