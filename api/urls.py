from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.UsersList.as_view()),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('spotify/', include('spotify.urls'))
]
