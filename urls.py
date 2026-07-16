from django.urls import path
from .views import test_signal, transaction_test

urlpatterns = [
    path("sync/", test_signal),
    path("transaction/", transaction_test),
]