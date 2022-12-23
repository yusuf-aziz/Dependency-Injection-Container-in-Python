"""Containers module."""

from dependency_injector import containers, providers
from apps.payment.service.debit_card_service import DebitCardPaymentService
from apps.payment.service.credit_card_service import CreditCardPaymentService
from apps.payment.repository.debit_card_payment_repository import DebitCardPaymentRepository
from apps.payment.repository.credit_card_payment_repository import CreditCardPaymentRepository


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    
    ############### Repository #####################
    debit_card_repo = providers.Singleton(
        DebitCardPaymentRepository,
        'mysql://localhost:3306/debit',
    )

    credit_card_repo = providers.Singleton(
        CreditCardPaymentRepository,
        'mysql://localhost:3306/credit',
    )

    ############### Service #####################

    debit_card_service = providers.Singleton(
        DebitCardPaymentService,
        debit_card_repo,
    )

    credit_card_service = providers.Singleton(
        CreditCardPaymentService,
        credit_card_repo,
    )
