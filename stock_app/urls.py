# stock_dashboard_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('create_watchlist/', views.create_watchlist, name='create_watchlist'),

    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
