from django.urls import path
from . import views

urlpatterns = [
    path('nuova-sezione/', views.CreaSezione.as_view(), name='crea-sezione'),
    path('sezione/<int:pk>/', views.visualizza_sezione, name='sezione_view')

]