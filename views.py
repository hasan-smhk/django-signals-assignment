import threading
import time

from django.db import transaction
from django.http import HttpResponse

from .models import Student


def test_signal(request):

    print("Caller Thread ID :", threading.get_ident())

    start = time.time()

    Student.objects.create(name="Hasan")

    end = time.time()

    print("Returned after :", end - start)

    return HttpResponse("Done")


def transaction_test(request):

    try:

        with transaction.atomic():

            Student.objects.create(name="Rollback Student")

            raise Exception("Rollback transaction")

    except Exception:
        pass

    count = Student.objects.filter(name="Rollback Student").count()

    return HttpResponse(f"Rows in DB = {count}")