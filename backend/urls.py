from django.contrib import admin
from django.urls import path, re_path, include
from users import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/users/$', views.users_list),
    re_path(r'^api/users/([0-9]+)$', views.users_detail),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('spotify/', include('spotify.urls'))
]
