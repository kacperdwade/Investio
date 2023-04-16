from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.home, name='home'),
    path('add_investment/', views.add_investment, name='add_investment'),
    path('investments/', views.user_investments, name='user_investments'),
]