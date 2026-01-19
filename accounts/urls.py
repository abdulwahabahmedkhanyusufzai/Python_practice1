from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountListView.as_view(), name='dashboard'),
    path('create/', views.AccountCreateView.as_view(), name='create_account'),
    path('account/<pk>/', views.AccountDetailView.as_view(), name='account_detail'),
    path('account/<pk>/deposit/', views.deposit_view, name='deposit'),
    path('account/<pk>/withdraw/', views.withdraw_view, name='withdraw'),
    path('account/<pk>/delete/', views.AccountDeleteView.as_view(), name='delete_account'),
]
