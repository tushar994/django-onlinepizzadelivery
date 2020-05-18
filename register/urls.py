from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "home"),
    path('login', views.login_r, name = 'login'),
    path('register', views.register, name = 'register'),
    path('register_result', views.register_result, name = 'register_result'),
    path('login_result', views.login_result, name = 'login_result'),
    path('logout_bro',views.logout_bro, name = 'logout_bro'),

]