from django.contrib import messages
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, TemplateView, DetailView, UpdateView

from invoices.forms import InvoiceForm
from invoices.models import Invoice
from profiles.models import Profile


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 2
    template_name = "invoices/main.html"

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)

        return super().get_queryset().filter(profile=profile).order_by('-created_at')


class InvoiceFormView(FormView):
    form_class = InvoiceForm
    template_name = 'invoices/create.html'
    i_instance = None

    def get_success_url(self):
        return reverse('invoices:simple_template', kwargs={'pk': self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)


class InvoiceTemplateView(DetailView):
    model = Invoice
    template_name = 'invoices/simple_template.html'


class InvoiceUpdateTemplate(UpdateView):
    model = Invoice
    template_name = 'invoices/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoices:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f"Invoice updated successfully --- {instance.invoice_number}")
        return super(InvoiceUpdateTemplate, self).form_valid(form)
