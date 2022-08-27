from django.http import HttpResponse

from invoices.models import Invoice


def hello_world(view):
    obj = Invoice.objects.get(id=1)
    print(obj.total_amount)
    return HttpResponse(obj)