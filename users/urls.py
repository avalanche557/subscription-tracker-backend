from django.urls import path

from .views import register_user, get_profile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', register_user),

    path('login/', TokenObtainPairView.as_view()),

    path('refresh/', TokenRefreshView.as_view()),

    path('profile/', get_profile),
]