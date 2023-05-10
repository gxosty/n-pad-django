from django.urls import path, include

from . import views

app_name = "account"

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
]