from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2023-09-29', customer_name='Test Customer')

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, 200)

    def test_get_single_invoice(self):
        response = self.client.get(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, 200)

    def test_create_invoice(self):
        data = {'date': '2023-09-30', 'customer_name': 'New Customer'}
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)  # 201 indicates successful creation

    def test_update_invoice(self):
        data = {'date': '2023-09-30', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/invoices/{self.invoice.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_invoice(self):
        response = self.client.delete(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, 204)  # 204 indicates successful deletion
