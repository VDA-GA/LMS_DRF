from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentRetrieveAPIView

app_name = UsersConfig.name


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_detail"),
]
