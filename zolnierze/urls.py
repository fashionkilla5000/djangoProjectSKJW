from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'zolnierze'
urlpatterns = [
    path('', views.ZolnierzListView.as_view(), name='list'),
    path('<int:pk>/', views.ZolnierzDetailView.as_view(), name='detail'),
    path('', views.KontraktyListView.as_view(), name='list'),
    path('<int:pk>/', views.KontraktyDetailView.as_view(), name='detail'),
    path('', views.PrzepustkiListView.as_view(), name='list'),
    path('<int:pk>/', views.PrzepustkiListView.as_view(), name='detail'),
    path('', views.WnioskiListView.as_view(), name='list'),
    path('<int:pk>/', views.WnioskiDetailView.as_view(), name='detail'),

    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

]