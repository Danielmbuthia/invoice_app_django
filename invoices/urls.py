from django.urls import path

from invoices import views

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='main'),
    path('create/', views.InvoiceFormView.as_view(), name='create'),
    # path('<pk>/', views.InvoiceTemplateView.as_view(), name='simple_template'),
    path('<pk>/', views.InvoiceAddPositionView.as_view(), name='details'),
    path('<pk>/update/', views.InvoiceUpdateTemplate.as_view(), name='update_invoice'),
    path('<pk>/close',views.InvoiceCloseView.as_view(),name='close_invoice'),
    path('<pk>/delete/<int:position_pk>/',views.InvoiceDeleteView.as_view(),name='delete_postion')
]
