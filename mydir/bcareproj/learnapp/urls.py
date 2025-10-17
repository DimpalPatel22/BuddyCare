from django.urls import path
from . import views

urlpatterns = [
    path('helplearn/', views.learn_home, name='learn'),
    path('emergency/', views.emergency, name='emergency'),
    path('food/', views.food, name='food'),
    path('owner/', views.owner, name='newowner'),
    path('health/', views.health, name='health'),
    path('dangerous/', views.dangerous, name='dangerous'),
    path('tipform/', views.tipform, name='tipform'),
]
