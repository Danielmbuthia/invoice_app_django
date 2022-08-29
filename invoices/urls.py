from django.urls import path

from invoices import views

urlpatterns = [
    path('', views.InvoiceListView.as_view()),
]
