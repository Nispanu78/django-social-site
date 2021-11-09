from django.urls import path
from . import views

urlpatterns = [
    path('nuova-sezione/', views.CreaSezione.as_view(), name='crea-sezione'),
    path('sezione/<int:pk>/', views.visualizza_sezione, name='sezione_view'),
    path('sezione/<int:pk>/crea-discussione/', views.crea_discussione, name='crea_discussione'),
    path('discussione/<int:pk>/', views.visualizza_discussione, name='visualizza_discussione'),
    path('sezione/<int:pk>/crea-discussione/rispondi/', views.aggiungi_risposta, name='rispondi_a_discussione'),

]
