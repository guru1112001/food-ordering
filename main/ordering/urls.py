from . import views
from django.urls import path

urlpatterns = [
    path("",views.menu,name="menu"),
    path("dashboard/",views.Dashboard , name="dashboard"),
    path("add_product/",views.add_product,name="add_product"),

    
]