from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.ad_list, name='list'),
    path('new/', views.ad_create, name='create'),
    path('<int:pk>/', views.ad_detail, name='detail'),
    path('<int:pk>/edit/', views.ad_edit, name='edit'),
    path('<int:pk>/delete/', views.ad_delete, name='delete'),
    path('statistic/', views.ad_statistic, name='statistic'),
]