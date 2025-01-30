from django.shortcuts import render
from django.db.models import Sum, Min, Max, F
from django.db.models.functions import TruncYear, TruncMonth, ExtractYear, ExtractMonth
from ..forms import CustomerSearchForm, DateRangeSearchForm
from ..models import Order


def sales_management(request):
    return render(request, 'business_management/SalesAssistSystem/SalesManagement/selection.html')

def annual_order_summary(request):
    form = CustomerSearchForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        customer_id = form.cleaned_data['query']

        orders = (
            Order.objects
            .filter(customer_id=customer_id)
            .annotate(order_year=ExtractYear('order_date'), order_month=ExtractMonth('order_date'))
            .values('customer_id', 'order_year', 'order_month')
            .annotate(
                total_quantity=Sum('quantity'),
                total_price=Sum(F('quantity') * F('item__price'))
            )
            .order_by('customer_id', 'order_year', 'order_month')
        )
        

        orders_by_year = {}
        for order in orders:
            year = order['order_year']
            if year not in orders_by_year:
                orders_by_year[year] = {
                    'orders': [],
                    'total_quantity_per_year': 0,
                    'total_price_per_year': 0,
                }
            orders_by_year[year]['orders'].append(order)
            orders_by_year[year]['total_quantity_per_year'] += order['total_quantity']
            orders_by_year[year]['total_price_per_year'] += order['total_price']

    else:
        orders_by_year = None

    return render(request, 'business_management/SalesAssistSystem/SalesManagement/annual_order_summary.html', {
        'orders_by_year': orders_by_year,
        'form': form,
    })


def product_wise_order_summary(request):
    form = CustomerSearchForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        customer_id = form.cleaned_data['query']

        products = (
            Order.objects
            .filter(customer_id=customer_id)
            .annotate(order_year=ExtractYear('order_date'))
            .values('order_year', 'item__id', 'item__name')
            .annotate(
                total_quantity=Sum('quantity'),
                total_price=Sum(F('quantity') * F('item__price'))
            )
            .order_by('order_year', 'item__id')
        )
        print(products)

        products_by_year = {}
        for product in products:
            year = product['order_year']
            if year not in products_by_year:
                products_by_year[year] = []
            products_by_year[year].append(product)

    else:
        products_by_year = None

    return render(request, 'business_management/SalesAssistSystem/SalesManagement/product_wise_order_summary.html', {
        'products_by_year': products_by_year,
        'form': form,
    })