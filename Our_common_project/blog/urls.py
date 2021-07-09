# posts/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    ]
