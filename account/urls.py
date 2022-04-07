from unicodedata import name
from django.urls import path
from .views import account_view, account, account_update, account_delete


urlpatterns = [
    path('', account_view, name='account_view'),
    path('account/', account, name='account'),
    path('update/', account_update, name='account_update'),
    path('delete/', account_delete, name='account_delete')
]