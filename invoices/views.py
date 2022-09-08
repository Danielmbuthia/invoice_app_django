from django.contrib import messages
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (
      ListView,
      FormView, 
      TemplateView,
      DetailView, 
      UpdateView,
      RedirectView,
      DeleteView
    )

from invoices.forms import InvoiceForm
from invoices.mixins import InvoiceNotClosed
from invoices.models import Invoice
from positions.forms import AddPositionsForm
from positions.models import Position
from profiles.models import Profile


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 4
    template_name = "invoices/main.html"

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)

        return super().get_queryset().filter(profile=profile).order_by('-created_at')


class InvoiceFormView(FormView):
    form_class = InvoiceForm
    template_name = 'invoices/create.html'
    i_instance = None

    def get_success_url(self):
        return reverse('invoices:details', kwargs={'pk': self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)


class InvoiceAddPositionView(InvoiceNotClosed, FormView):
    form_class = AddPositionsForm
    template_name = 'invoices/details.html'

    def form_valid(self, form):
        invoice_pk = self.kwargs.get('pk')
        invoice = Invoice.objects.get(pk= invoice_pk)
        instance = form.save(commit=False)
        instance.invoice = invoice
        form.save()
        messages.info(self.request, f'Invoice position added successfully. {instance.title}')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice_obj = Invoice.objects.get(pk = self.kwargs.get('pk'))
        positons = invoice_obj.positions
        context["obj"] = invoice_obj 
        context["positions"] = positons 
        return context
    
class InvoiceTemplateView(DetailView):
    model = Invoice
    template_name = 'invoices/simple_template.html'


class InvoiceUpdateTemplate(InvoiceNotClosed,UpdateView):
    model = Invoice
    template_name = 'invoices/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoices:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f"Invoice updated successfully --- {instance.invoice_number}")
        return super(InvoiceUpdateTemplate, self).form_valid(form)


class InvoiceCloseView(RedirectView):
    pattern_name = 'invoices:details'

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk=pk)
        obj.closed = True
        obj.save()
        return super().get_redirect_url(*args, **kwargs)

class InvoiceDeleteView(InvoiceNotClosed,DeleteView):
    model = Position

    template_name = 'invoices/position_confirm_delete.html'

    def get_object(self):
        pk = self.kwargs.get('position_pk')
        obj = Position.objects.get(pk=pk) 
        return obj

    def get_success_url(self):
        messages.info(self.request, f'Position deleted successfully {self.object.title}')
        return reverse('invoices:details', kwargs={'pk':self.object.invoice.pk})
