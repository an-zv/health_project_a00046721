from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def total_amount(self):
        total = 0
        for item in self.invoiceitem_set.all():
            total += item.line_total()
        return total
    
    def __str__(self):
        return f"Invoice for {self.id} - {self.patient.name}"
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def line_total(self):
        return self.service.price * self.quantity

    def __str__(self):
        return f"{self.service.name} x {self.quantity}"
