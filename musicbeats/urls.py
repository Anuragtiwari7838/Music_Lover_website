from django.urls import path
from .import views

urlpatterns = [
    path('songs',views.songs,name='songs'),
    path('songs/<int:id>',views.songpost,name='songpost'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('watchlater',views.watchlater,name='watchlater'),
    path('history',views.history,name='history'),
    path('singer',views.singer,name='singer'),
    path('dhillon',views.dhillon,name='dhillon'),
    path('neha',views.neha,name='neha'),
    path('sonu',views.sonu,name='sonu'),
    path('search',views.search,name='search'),
] 