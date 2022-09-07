from django.urls import path

from invoices import views

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='main'),
    path('create/', views.InvoiceFormView.as_view(), name='create'),
    path('<pk>/', views.InvoiceTemplateView.as_view(), name='simple_template'),
    path('<pk>/update/', views.InvoiceUpdateTemplate.as_view(), name='update_invoice'),
]
