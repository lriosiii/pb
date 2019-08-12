from django.shortcuts import render
from django.views.generic.base import TemplateView


class AccountingHome(TemplateView):
    template_name = 'accounting/home.html'