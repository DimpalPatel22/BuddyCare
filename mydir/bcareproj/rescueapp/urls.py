from django.urls import path
from . import views

urlpatterns = [
    path('', views.rescue_page_view, name='rescue_page'),
    path('form/', views.rescue_form_view, name='rescue_form'),
    path('list/', views.rescue_list_view, name='rescue_list'),
]
