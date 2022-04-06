from unicodedata import name
from django.urls import path
from .views import account_view, account


urlpatterns = [
    path('', account_view, name='account_view'),
    path('account/', account, name='account'),
]