from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name='home'),
    path('addInvestment/', views.addInvestment, name='add_investment'),
    path('Investments/', views.userInvestments, name='user_investments'),
    path('about/', views.about, name='about'),
]