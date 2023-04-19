from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('investment/<int:id_>/', views.investment_detail_view, name='investment-detail-view'),
    path('add_investment/', views.add_investment, name='add_investment'),
    path('investments/', views.user_investments, name='user_investments'),
    path('edit/<int:id>/', views.edit_investment, name='edit_investment')
]
