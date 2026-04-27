from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Service, Invoice
from .forms import PatientForm, ServiceForm, InvoiceForm, InvoiceItemForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def is_recepcionist(user):
    return user.groups.filter(name='Recepcionist').exists() or user.is_superuser

def is_doctor(user):
    return user.groups.filter(name='Doctor').exists() or user.is_superuser

def is_accountant(user):
    return user.groups.filter(name='Accountant').exists() or user.is_superuser

@login_required
def home(request):
    return render(request, 'clinic/home.html')

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinic/patient_list.html', {'patients': patients})

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'clinic/service_list.html', {'services': services})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'clinic/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'clinic/invoice_detail.html', {'invoice': invoice})

@login_required
@user_passes_test(is_recepcionist)
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinic:patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinic/form.html', {'form': form, 'title': 'Create Patient'})

@login_required
@user_passes_test(is_accountant)
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinic:service_list')
    else:
        form = ServiceForm()
    return render(request, 'clinic/form.html', {'form': form, 'title': 'Create Service'})

@login_required
@user_passes_test(is_recepcionist)
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('clinic:invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm()
    return render(request, 'clinic/form.html', {'form': form, 'title': 'Create Invoice'})

@login_required
@user_passes_test(is_accountant)
def invoice_item_create(request):
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('clinic:invoice_detail', invoice_id = item.invoice.id)
    else:
        form = InvoiceItemForm()
    return render(request, 'clinic/form.html', {'form': form, 'title': 'Add Invoice Item'})