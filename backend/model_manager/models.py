from django.db import models


class InvoiceManager(models.Manager):
    def get_invoice_data_count(self) -> int:
        return Invoice.objects.all().count()


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_amount = models.IntegerField()

    objects = InvoiceManager()

    def __str__(self) -> str:
        return f"{self.invoice_number}-{self.invoice_date}-{self.invoice_amount}"
