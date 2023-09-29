from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice_details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('invoice_details/<int:pk>/', InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]

# method 2nd

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoices-detail', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
