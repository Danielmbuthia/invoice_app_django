from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from invoices.forms import InvoiceForm
from invoices.models import Invoice
from profiles.models import Profile


class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/main.html"

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)

        return super().get_queryset().filter(profile=profile).order_by('-created_at')


class InvoiceFormView(FormView):
    form_class = InvoiceForm
    template_name = 'invoices/create.html'
    success_url = reverse_lazy('invoices:main')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        return super().form_valid(form)
