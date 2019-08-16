from django import forms


class NBRevenueForm(forms.Form):
    nb_form = forms.FileField(allow_empty_file=False)
    revenue_form = forms.FileField(allow_empty_file=False)


