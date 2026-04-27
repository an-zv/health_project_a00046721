from django.test import TestCase
from .models import Patient, Service, Invoice, InvoiceItem
from django.urls import reverse
from django.contrib.auth.models import User, Group

# Create your tests here.

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            name='Rebeca',
            email='rebeca@gmail.com',
            phone='654321987'
        )
        self.service = Service.objects.create(
            name='General Consultation',
            price=50.00
        )
        self.invoice = Invoice.objects.create(
            patient=self.patient,
            status='pending',
        )

    def test_invoice_total_amount(self):
        InvoiceItem.objects.create(
            invoice=self.invoice,
            service=self.service,
            quantity=3
        )
        self.assertEqual(self.invoice.total_amount(), 150.00)

    def test_invoice_item_line_total(self):
        item = InvoiceItem.objects.create(
            invoice=self.invoice,
            service=self.service,
            quantity=2
        )
        self.assertEqual(item.line_total(), 100.00)

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_page_loads(self):
        response = self.client.get(reverse('clinic:home'))
        self.assertEqual(response.status_code, 200)

    def test_patient_list_loads(self):
        response = self.client.get(reverse('clinic:patient_list'))
        self.assertEqual(response.status_code, 200)

    def test_service_list_loads(self):
        response = self.client.get(reverse('clinic:service_list'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_list_loads(self):
        response = self.client.get(reverse('clinic:invoice_list'))
        self.assertEqual(response.status_code, 200)
    
class PermissionTests(TestCase):
    def setUp(self):
        self.recepcionist_group = Group.objects.create(name='Recepcionist')
        self.accountant_group = Group.objects.create(name='Accountant')

        self.recepcionist_user = User.objects.create_user(
            username='recepcionist1',
            password='rec12345')
        self.recepcionist_user.groups.add(self.recepcionist_group)

        self.accountant_user = User.objects.create_user(
            username='accountant1', 
            password='acc12345')
        self.accountant_user.groups.add(self.accountant_group)

    def test_recepcionist_access(self):
        self.client.login(username='recepcionist1', password='rec12345')
        response = self.client.get(reverse('clinic:patient_create'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_accountant_access(self):
        self.client.login(username='accountant1', password='acc12345')
        response = self.client.get(reverse('clinic:service_create'))
        self.assertEqual(response.status_code, 200)