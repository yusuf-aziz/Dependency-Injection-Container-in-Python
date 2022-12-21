Django + Dependency Injector Example
====================================

This is a `Django <https://www.djangoproject.com/>`_ +
`Dependency Injector <https://python-dependency-injector.ets-labs.org/>`_ example application.

We'll start by creating view, service and repository classes for the payment module.
The payment-service class is being injected into the "view" in this instance, and dependency injection will be useful if we decide to switch from DebitCardPayment to CreditCardPayment in the future.

