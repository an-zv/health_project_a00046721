from django.urls import path
from . import views

app_name = 'clinic'

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('services/', views.service_list, name='service_list'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('services/create/', views.service_create, name='service_create'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoice-items/create/', views.invoice_item_create, name='invoice_item_create'),
]