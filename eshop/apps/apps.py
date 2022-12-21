"""Application config module."""

from django.apps import AppConfig
from eshop import container

class PaymentConfig(AppConfig):
    name = "apps"

    def ready(self):
        container.wire(modules=[".payment.api.views"])
