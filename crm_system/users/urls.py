from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register_view
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect
app_name = 'users'

class GetLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', GetLogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]