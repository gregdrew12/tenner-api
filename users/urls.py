from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<str:identifier>/', views.UserDetail.as_view(), name='user-detail'),
    path('<str:identifier>/followers/', views.FollowerList.as_view(), name='user-followers-list'),
    path('<str:identifier>/follow/', views.FollowView.as_view(), name='user-follow'),
]