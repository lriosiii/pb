from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import NBRevenueForm
import csv
import openpyxl


class AccountingHome(TemplateView):
    template_name = 'accounting/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NBRevenueForm'] = NBRevenueForm
        return context

    def post(self, request, *args, **kwargs):
        nb_input_file = request.FILES['nb_form']
        nb_wb = openpyxl.load_workbook(nb_input_file)
        nb_worksheet = nb_wb['JulyRev']  # TODO month

        revenue_file_input = request.FILES['revenue_form']
        revenue_wb = openpyxl.load_workbook(revenue_file_input, read_only=True)
        revenue_worksheet = revenue_wb['Reconciliation Report']