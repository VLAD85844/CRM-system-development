from django.urls import path
from . import views

app_name = 'contracts'

urlpatterns = [
    path('', views.contract_list, name='list'),
    path('new/', views.contract_create, name='create'),
    path('<int:pk>/', views.contract_detail, name='detail'),
    path('<int:pk>/edit/', views.contract_edit, name='edit'),
    path('<int:pk>/delete/', views.contract_delete, name='delete'),
]