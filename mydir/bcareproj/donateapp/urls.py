from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate_view, name='donate'),
    path('offline/', views.offline_donate, name='offline_donate'),
    path('success/', views.donation_success, name='donation_success'),
    path('payment/', views.payment_view, name='payment'),
    path('process_payment/', views.process_payment, name='process_payment')

]
