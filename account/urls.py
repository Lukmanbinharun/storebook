from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.userlogin, name='login'),
    path('singin', views.ragestation, name='singup'),
    path('logout', views.userlogout, name='logout'),
    path('profile', views.profile, name='profile'),
]