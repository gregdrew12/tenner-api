from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('logout/', views.LogoutView.as_view(), name ='user-logout')
]