from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage' ),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/<str:username>/', views.user_profile_view, name='user_profile'),
    path('cerca/', views.cerca, name='funzione_cerca'),
]
