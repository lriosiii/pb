from django import forms


class CompareNbRevenueForm(forms.Form):
    nb_file = forms.FileField(allow_empty_file=False, label="New Biz")
    reconciliation_file = forms.FileField(allow_empty_file=False, label="Reconciliation")


class CompareRenewalsRevenueForm(forms.Form):
    renewals_file = forms.FileField(allow_empty_file=False, label="Renewals")
    reconciliation_file = forms.FileField(allow_empty_file=False, label="Reconciliation")


class CompareGovgisticsAndRevenueForm(forms.Form):
    govgistics_file = forms.FileField(allow_empty_file=False, label='Govgistics')
    reconciliation_file = forms.FileField(allow_empty_file=False, label='Reconciliation')
