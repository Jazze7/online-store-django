from django.urls import path
from web import views


app_name = "web"

urlpatterns = [
    path('', views.index, name="index"),
    path('admin-view/', views.admin_view, name="admin_view"),

]
