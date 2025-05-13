from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    account_manager_image = models.CharField(max_length=255)
    sales_manager_image = models.CharField(max_length=255)
    account_manager = models.CharField(max_length=255)
    sales_manager = models.CharField(max_length=255)
    start_date = models.DateField()
    status = models.CharField(max_length=20)
    type_of_client = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    monthly_budgets = models.CharField(max_length=50)
    balance_usd = models.DecimalField(max_digits=10, decimal_places=2)
    balance_rub = models.DecimalField(max_digits=10, decimal_places=2)
    loans_rub = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'client_module_table_0001_client'


class Offer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offers')
    title = models.CharField(max_length=255)
    sources = ArrayField(models.CharField(max_length=255), default=list)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'
        db_table = 'client_module_table_0002_offer'


class PaymentTerm(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payment_terms')
    payment_method = models.CharField(max_length=50)
    exchange_extras = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Условие оплаты'
        verbose_name_plural = 'Условия оплаты'
        db_table = 'client_module_table_0003_payment_term'
