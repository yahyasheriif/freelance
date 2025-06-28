from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True,blank=True)

    date = models.DateField(default=models.DateField(auto_now_add=True))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices')
    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())
    @property
    def total_paid(self):
        return sum(payment.amount for payment in self.payments.all())
    @property
    def balance_due(self):
        return self.total_amount - self.total_paid
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], default='draft')
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.invoice_number:
            self.invoice_number = f"INV-{self.id}"
            super().save(update_fields=['invoice_number'])

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    method = models.CharField(max_length=20, choices=[
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('other', 'Other')
    ])
    def __str__(self):
        return f"Payment for {self.invoice.invoice_number} - {self.amount}"
    
class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.description} - {self.quantity}  {self.unit_price}"
    
    @property
    def total_price(self):
        return self.quantity * self.unit_price
