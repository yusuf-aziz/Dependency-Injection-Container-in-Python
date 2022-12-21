import logging
from abc import abstractmethod
from apps.payment.dto.payment_dtos import PaymentRequestDTO, PaymentResponseDTO


class BasePaymentService:

    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
    
    @abstractmethod
    def pay(self, payment_request_dto: PaymentRequestDTO) -> PaymentResponseDTO:
        raise NotImplementedError(self.__class__.__name__)    
