from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('index/duo', views.duoindex, name="duoindex"),
    path('signup/player', views.playersign, name="player"),
    path('signup/duo', views.duosign, name="duosign"),
    path('deleteduo/<int:id>', views.deleteduo, name="deleteduo"),
    path('deleteplayer/<int:id>', views.deleteplayer, name="deleteplayer"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/duo/yourpage', views.yourduo, name='yourduo'),
]
