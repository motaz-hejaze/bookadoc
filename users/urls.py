from django.urls import path
from . import views
from rest_framework_simplejwt import views as user_views

urlpatterns = [
    path('token/', user_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', user_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/' , views.HomeView.as_view() , name='home'),
]