
from django.contrib import admin
from django.urls import path,include
from account import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.RegisterPage,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="account/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="account/logout.html"),name="logout"),
    path("",include("ordering.urls")),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


