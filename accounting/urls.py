from django.urls import path
from .views import AccountingHome


app_name = 'accounting'

urlpatterns = [
    path(r'', AccountingHome.as_view(), name='accountinghome')
]