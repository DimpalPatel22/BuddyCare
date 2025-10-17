from django.urls import path
from . import views

urlpatterns = [
    path('', views.adopt_page, name='adopt_page'),
    path('adopt-form/', views.adopt_form, name='adopt_form'),
    path('success/', views.adopt_success, name='adopt_success'),
]
