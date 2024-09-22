from django.db import models

class Address(models.Model):
    address = models.TextField()
    addr_type = models.CharField(max_length=50)
    date_reported = models.DateTimeField()
    sno = models.CharField(max_length=10)

class ClassificationInsType(models.Model):
    amount_overdue = models.DecimalField(max_digits=15, decimal_places=2)
    approved_credit_sanctioned = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)
    institution_type = models.CharField(max_length=100)
    legal_flag = models.CharField(max_length=10)
    no_of_accounts = models.IntegerField()
    outstanding_balance = models.DecimalField(max_digits=15, decimal_places=2)

class ClassificationProdType(models.Model):
    amount_overdue = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)
    no_acc_last_six_mon = models.IntegerField()
    no_of_accounts = models.IntegerField()
    product_type = models.CharField(max_length=100)
    sanctioned_amount = models.DecimalField(max_digits=15, decimal_places=2)
    total_outstanding_balance = models.DecimalField(max_digits=15, decimal_places=2)

class ClosedAccount(models.Model):
    account_status = models.CharField(max_length=50)
    cf_closing_date = models.DateTimeField()
    credit_facility_type = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=200)
    legal_action_status = models.CharField(max_length=50)
    sanction_amount = models.DecimalField(max_digits=15, decimal_places=2)
    sno = models.CharField(max_length=10)

class ConsCommDetails(models.Model):
    expiry_date = models.DateTimeField(null=True, blank=True)
    identifier_number = models.CharField(max_length=50)
    id_type = models.CharField(max_length=100)
