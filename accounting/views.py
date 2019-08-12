from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import NBForm, RevenueForm


class AccountingHome(TemplateView):
    template_name = 'accounting/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NBForm'] = NBForm
        context['RevenueForm'] = RevenueForm
        return context
