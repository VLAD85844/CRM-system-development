from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='list'),
    path('new/', views.lead_create, name='create'),
    path('<int:pk>/', views.lead_detail, name='detail'),
    path('<int:pk>/edit/', views.lead_edit, name='edit'),
    path('<int:pk>/delete/', views.lead_delete, name='delete'),
]