from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  #get the access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #get the refresh token
    path('signup/',views.SignupView.as_view(),name="sign_up")
]