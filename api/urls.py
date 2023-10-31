from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', 
        jwt_views.TokenObtainPairView.as_view(), 
        name ='token-obtain-pair'),
    path('token/refresh/', 
        jwt_views.TokenRefreshView.as_view(), 
        name ='token-refresh'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('users/', include('users.urls')),
    path('spotify/', include('spotify.urls'))
]
