from django import forms


class CompareNbRevenueForm(forms.Form):
    nb_file = forms.FileField(allow_empty_file=False)
    reconciliation_file = forms.FileField(allow_empty_file=False)


