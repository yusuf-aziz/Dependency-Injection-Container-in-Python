from dependency_injector.wiring import inject, Provide
from eshop.containers import Container
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from apps.payment.service.base_payment_service import BasePaymentService
from apps.payment.dto.payment_dtos import PaymentRequestDTO


class PaymentView(APIView):

    @inject
    def __init__(self, payment_service: BasePaymentService = Provide[Container.credit_card_service]):
        self.payment_service = payment_service

    def get(self, request):
        return Response({'message': 'Ok'}, status=200)

    def post(self, request, *args, **kwargs):

        payment_request_dto = json.loads(json.dumps(
            request.data), object_hook=PaymentRequestDTO)

        payment_response_dto = self.payment_service.pay(payment_request_dto)

        return Response(json.dumps(payment_response_dto.__dict__), status=200)
