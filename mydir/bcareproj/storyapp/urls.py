from django.urls import path
from . import views

urlpatterns = [
    path('', views.stories, name='stories'),
    path('sharestory/', views.sharestory, name='sharestory'),
]
