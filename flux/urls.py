from django.urls import path

from . import views

urlpatterns = [
    path('flux/', views.flux, name='flux'),
    path('critique/', views.critic, name='critic'),
    path('posts/', views.posts, name='posts'),
    path('abonnements/', views.subs, name='subs'),
    path('ticket/', views.ticket, name='ticket'),
    path('commentaire/', views.comment, name='comment'),
]

