from users import views
from django.urls import path


app_name = "users"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('admin-login/', views.admin_login, name="admin_login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),

]