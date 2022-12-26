
from django.contrib import admin
from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.RegisterPage,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="account/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="account/logout.html"),name="logout"),
]
