from django.contrib import admin
from .models import Patient, Doctor, Service, Invoice, InvoiceItem
# Register your models here.

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__name',)
    inlines = [InvoiceItemInline]


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)