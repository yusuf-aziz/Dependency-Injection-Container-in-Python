from django.urls import path
from apps.payment.api.views import PaymentView

app_name = "payment"

urlpatterns = [
    path('', PaymentView.as_view()),
]
