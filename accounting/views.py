from django.views.generic.base import TemplateView
from .forms import CompareNbRevenueForm
import openpyxl
from django.http import HttpResponse
from openpyxl.writer.excel import save_virtual_workbook
import datetime


class AccountingHome(TemplateView):
    template_name = 'accounting/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NBRevenueForm'] = CompareNbRevenueForm
        return context

    def post(self, request, *args, **kwargs):
        from openpyxl.styles import Font
        from openpyxl.styles.colors import RED

        nb_input_file = request.FILES['nb_file']
        nb_wb = openpyxl.load_workbook(nb_input_file)
        monthrev = nb_wb.sheetnames[4]
        nb_worksheet = nb_wb[monthrev]
        nb_filled_rows = (row for row in nb_worksheet if row[3].value)
        next(nb_filled_rows)

        revenue_file_input = request.FILES['reconciliation_file']
        revenue_wb = openpyxl.load_workbook(revenue_file_input, read_only=True, data_only=True)

        rev_accounts = {str(row[5].value).lower() for row in revenue_wb.active.rows if row[5].value}

        for row in nb_filled_rows:
            if str(row[3].value).lower() in rev_accounts:
                continue
            else:
                for cell in row:
                    cell.font = Font(color=RED)

        response = HttpResponse(content=save_virtual_workbook(nb_wb), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
        return response

