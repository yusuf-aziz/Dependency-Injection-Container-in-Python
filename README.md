# Dependency-Injection-Container-in-Python
Dependency Injection Container in Python
This is a Django + Dependency Injector example application.

Dependency Injection Container in Python

Writing clean, maintainable code is a challenging task, but fortunately, there are many patterns and techniques to make achieving that task much easier. Dependency Injection is one of those approaches to writing highly effective and loosely coupled code.

We’ll start by creating view, service and repository classes for the payment module.

The payment-service class is being injected into the “view” in this instance, and dependency injection will be useful if we decide to switch from DebitCardPayment to CreditCardPayment in the future.
