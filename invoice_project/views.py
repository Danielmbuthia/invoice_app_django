from django.http import HttpResponse
from django.shortcuts import render

from invoices.models import Invoice


def hello_world(request):
    obj = Invoice.objects.get(id=1)
    print(obj.total_amount)
    return render(request, 'home.html', {})
