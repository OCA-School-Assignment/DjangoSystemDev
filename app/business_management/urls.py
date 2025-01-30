from django.urls import path
# from . import business_management
# from .. import business_management
from .decorators import department_required
from business_management import urls
from .views.authentication_views import index, logout_view, home, test
from .views.department_views import department_management, DepartmentListView, department_register, department_edit, department_delete
from .views.product_views import product_management, product_register, product_delete, product_edit, ProductListView
from .views.production_views import production_management, production_register, production_delete, production_edit, ProductionListView
from .views.stock_views import StockListView
from .views.shipment_views import ShipmentLogListView, shipment_test
from .views.employee_views import employee_management, employee_register, employee_delete, employee_edit, EmployeeListView
from .views.customer_views import customer_management, customer_register, customer_delete, customer_edit, CustomerListView
from .views.order_views import order_management, order_register, order_delete, order_edit, OrderListView
from .views.sales_views import sales_management, annual_order_summary, product_wise_order_summary


urlpatterns = [
    path('' , index, name='index'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('employee-management/', department_required(employee_management, ['Human Resources']), name='employee-management'),
    path('employee-management/register/', employee_register, name='employee-register'),
    path('employee-management/delete/<str:employee_id>/', employee_delete, name='employee-delete'),
    path('employee-management/edit/<str:employee_id>/', employee_edit, name='employee-edit'),
    path('employee-management/manage', EmployeeListView.as_view(), name='employee-manage'),
    path('department-management/', department_required(department_management, ['Human Resources']), name='department-management'),
    path('department-management/manage/', DepartmentListView.as_view(), name='department-manage'),
    path('department-management/register/', department_register, name='department-register'),
    path('department-management/delete/<str:department_id>/', department_delete, name='department-delete'),
    path('department-management/edit/<str:department_id>/', department_edit, name='department-edit'),
    path('stock-management/', department_required(StockListView.as_view(), ['Product Management', 'Production Management']), name='stock-management'),
    path('product-management/', department_required(product_management, ['Product Management', 'Sales']), name='product-management'),
    path('product-management/register/', department_required(product_register, ['Product Management']), name='product-register'),
    path('product-management/delete/<str:product_id>/', department_required(product_delete, ['Product Management']), name='product-delete'),
    path('product-management/edit/<str:product_id>/', department_required(product_edit, ['Product Management']), name='product-edit'),
    path('product-management/manage/', department_required(ProductListView.as_view(), ['Product Management', 'Sales']), name='product-manage'),
    path('shipment-management/', department_required(ShipmentLogListView.as_view(), ['Product Management', 'Production Management']), name='shipment-management'),
    path('production-management/', production_management, name='production-management'),
    path('production-management/register/', department_required(production_register, ['Production Management']), name='production-register'),
    path('production-management/delete/<str:production_id>/', department_required(production_delete, ['Production Management']), name='production-delete'),
    path('production-management/edit/<str:production_id>/', department_required(production_edit, ['Production Management']), name='production-edit'),
    path('production-management/manage/', department_required(ProductionListView.as_view(), ['Production Management']), name='production-manage'),
    path('customer-management/', department_required(customer_management, ['Sales']), name='customer-management'),
    path('customer-management/register/', department_required(customer_register, ['Sales']), name='customer-register'),
    path('customer-management/delete/<str:customer_id>/', department_required(customer_delete, ['Sales']), name='customer-delete'),
    path('customer-management/edit/<str:customer_id>/', department_required(customer_edit, ['Sales']), name='customer-edit'),
    path('customer-management/manage/', department_required(CustomerListView.as_view(), ['Sales']), name='customer-manage'),
    path('order-management/', department_required(order_management, ['Sales']), name='order-management'),
    path('order-management/register/', department_required(order_register, ['Sales']), name='order-register'),
    path('order-management/delete/<str:order_id>/', department_required(order_delete, ['Sales']), name='order-delete'),
    path('order-management/edit/<str:order_id>/', department_required(order_edit, ['Sales']), name='order-edit'),
    path('order-management/manage/', department_required(OrderListView.as_view(), ['Sales']), name='order-manage'),
    path('sales-management/', department_required(sales_management, ['Sales']), name='sales-management'),
    path('sales-management/annual-order-summary/', department_required(annual_order_summary, ['Sales']), name='annual-order-summary'),
    path('sales-management/product-wise-order-summary/', department_required(product_wise_order_summary, ['Sales']), name='product-wise-order-summary'),
]