from django.urls import path
from . import views

urlpatterns=[
    path('', views.volunteer_home, name='volunteer'),
    path('join/', views.joingroup_form, name='groupform'),
]