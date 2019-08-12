from django import forms


class NBForm(forms.Form):
    file = forms.FileField(allow_empty_file=False)


class RevenueForm(forms.Form):
    file = forms.FileField(allow_empty_file=False)



