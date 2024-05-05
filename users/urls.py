from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentListAPIView,
    PaymentRetrieveAPIView,
    SubscriptionAPIView,
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(permission_classes=[AllowAny]), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("list/", UserListAPIView.as_view(), name="users_list"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_detail"),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
]
