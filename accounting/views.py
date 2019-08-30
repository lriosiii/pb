from django.views.generic.base import TemplateView
from .forms import CompareNbRevenueForm, CompareRenewalsRevenueForm
import openpyxl
from django.http import HttpResponse
from openpyxl.writer.excel import save_virtual_workbook
import datetime


class AccountingHome(TemplateView):
    template_name = 'accounting/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NBRevenueForm'] = CompareNbRevenueForm
        context['CompareRenewalsRevenueForm'] = CompareRenewalsRevenueForm
        return context

    def post(self, request, *args, **kwargs):
        from openpyxl.styles import Font
        from openpyxl.styles.colors import RED

        revenue_file_input = request.FILES['reconciliation_file']
        revenue_wb = openpyxl.load_workbook(revenue_file_input, read_only=True, data_only=True)
        rev_accounts = {str(row[5].value).lower() for row in revenue_wb.active.rows if row[5].value}

        if request.POST.get('newbiz'):
            resp_wb = openpyxl.load_workbook(request.FILES['nb_file'])
            monthrev = resp_wb.sheetnames[4]
            nb_worksheet = resp_wb[monthrev]
            data_rows = (row for row in nb_worksheet if row[3].value)
            next(data_rows)
            for row in data_rows:
                if str(row[3].value).lower() in rev_accounts:
                    continue
                else:
                    for cell in row:
                        cell.font = Font(color=RED)
        if request.POST.get('renewals'):
            resp_wb = openpyxl.load_workbook(request.FILES['renewals_file'])
            sheet12 = resp_wb.sheetnames[11]
            worksheet = resp_wb[sheet12]
            data_rows = (row for row in worksheet if row[2].value)
            next(data_rows)
            for row in data_rows:
                if str(row[2].value).lower() in rev_accounts:
                    continue
                else:
                    for cell in row:
                        cell.font = Font(color=RED)


        response = HttpResponse(content=save_virtual_workbook(resp_wb), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
        return response

