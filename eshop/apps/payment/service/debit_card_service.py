from .base_payment_service import BasePaymentService
from apps.payment.dto.payment_dtos import PaymentRequestDTO, PaymentResponseDTO
import random
from datetime import datetime
from apps.payment.repository.debit_card_payment_repository import DebitCardPaymentRepository


class DebitCardPaymentService(BasePaymentService):

    def __init__(self, debit_card_repo: DebitCardPaymentRepository) -> None:
        super().__init__()
        self.debit_card_repo = debit_card_repo

    def pay(self, request_dto: PaymentRequestDTO) -> PaymentResponseDTO:        

        # convert to model
        model_data = self._get_payment_model(request_dto)
        # saving model using repository
        self.debit_card_repo.save(model_data)

        self.logger.debug("payment %s has been paid by the DebitCardcls", request_dto)

        # dummy response
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        response_dto = PaymentResponseDTO(random.randint(
            99999, 9999999), request_dto.order_id, dt_string, 'Debit-Card')      

        return response_dto

    def _get_payment_model(self, request_dto: PaymentRequestDTO) -> dict:
        model_data = {
            'order_id' : request_dto.order_id, 
            'amount' : request_dto.amount
        }

        return model_data
