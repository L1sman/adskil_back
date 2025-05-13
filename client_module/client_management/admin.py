from django.contrib import admin
from .models import Client, Offer, PaymentTerm


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'account_manager', 'sales_manager', 'start_date',
        'status', 'type_of_client', 'experience',
        'monthly_budgets', 'balance_usd', 'balance_rub', 'loans_rub'
    )
    search_fields = ('name', 'account_manager', 'sales_manager')
    list_filter = ('status', 'type_of_client', 'experience')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('client', 'title', 'spend', 'profit', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    autocomplete_fields = ['client']


@admin.register(PaymentTerm)
class PaymentTermAdmin(admin.ModelAdmin):
    list_display = ('client', 'payment_method', 'exchange_extras', 'vat', 'start_date', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('payment_method',)
    autocomplete_fields = ['client']
