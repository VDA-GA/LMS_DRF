from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course
from users.models import Payment, Subscription, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_product, create_stripe_session


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("course", "lesson", "method")
    ordering_fields = ("date",)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user, method="перевод на карту")
        product = create_stripe_product(payment.course)
        price = create_stripe_price(product=product, amount=payment.amount)
        session_id, session_url = create_stripe_session(price)
        payment.session_id = session_id
        payment.payment_link = session_url
        payment.save()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class SubscriptionAPIView(APIView):
    @swagger_auto_schema(operation_description="Add or remove the subscription on a course")
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("id")
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(user=user).filter(course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        return Response({"message": message})
