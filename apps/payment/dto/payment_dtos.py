from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentRequestDTO:
    order_id: int = None
    amount: float = None
    description: str = None
    date_time: str = None

@dataclass
class PaymentResponseDTO:
    payment_id: int = None
    order_id: int = None   
    date_time: str = None
    payment_method : str = None
