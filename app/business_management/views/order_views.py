from ..models import Order
from ..forms import OrderSearchForm, OrderRegisterForm, OrderEditForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def order_management(request):
    return render(request, 'business_management/SalesAssistSystem/OrderManagement/selection.html')


class OrderListView(ListView):
    model = Order
    template_name = 'business_management/SalesAssistSystem/OrderManagement/order_management.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = OrderSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        query = self.request.GET.get('query', '')
        search_type = self.request.GET.get('search_type', '')
        
        if search_type == 'id' and query:
            if not query.isdigit():
                messages.error(self.request, '受注IDは整数で入力してください。')
                return queryset.none()
            queryset = queryset.filter(id=query).order_by('id')
        elif search_type == 'customer_name' and query:
            queryset = queryset.filter(customer__name__icontains=query).order_by('id')
        
        return queryset


def order_register(request):    
    params = {
        'form': OrderRegisterForm()
    }
    if request.method == 'POST':
        form = OrderRegisterForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            messages.success(request, f'受注ID:「{order.id}」、得意先名:「{order.customer.name}」を登録しました。')
            return redirect('/order-management/register')
        else:
            messages.error(request, '受注IDまたは得意先名が既に登録されています。')
            return redirect('/order-management/register')
    return render(request, 'business_management/SalesAssistSystem/OrderManagement/order_register.html', params)


def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    params = {
        'form': OrderEditForm(instance=order),
        'order': order,
    }
    if request.method == 'POST':
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'受注ID:「{order.id}」、得意先名:「{order.customer.name}」を更新しました。')
            return redirect('order-manage')
    return render(request, 'business_management/SalesAssistSystem/OrderManagement/order_edit.html', params)


def order_delete(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        deleted_order_id = order.id
        deleted_customer_name = order.customer.name
        order.delete()
        messages.error(request, f'受注ID:「{deleted_order_id}」、得意先名:「{deleted_customer_name}」を削除しました。')
    return redirect('order-manage')
