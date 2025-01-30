from ..models import Customer
from ..forms import CustomerSearchForm, CustomerRegisterForm, CustomerEditForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.utils import IntegrityError

def customer_management(request):
    return render(request, 'business_management/SalesAssistSystem/CustomerManagement/selection.html')


class CustomerListView(ListView):
    model = Customer
    template_name = 'business_management/SalesAssistSystem/CustomerManagement/customer_management.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CustomerSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # search_type = self.request.GET.get('search_type', '')
        query = self.request.GET.get('query', '')
        
        if query:
            queryset = queryset.filter(id=query)
        # if search_type == 'id' and query:
        #     queryset = queryset.filter(id=query)
        # elif search_type == 'name' and query:
            # queryset = queryset.filter(name__icontains=query)
        
        return queryset


def customer_register(request):    
    params = {
        'form': CustomerRegisterForm()
    }
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            try:
                customer = form.save(commit=False)
                customer.save()
                messages.success(request, f'得意先ID:「{customer.id}」、従業員名:「{customer.name}」を登録しました。')
                return redirect('/employee-management/register')
            except IntegrityError:
                messages.error(request, '得意先IDまたはメールアドレスが既に登録されています。')
                return redirect('/customer-management/register')
    return render(request, 'business_management/SalesAssistSystem/CustomerManagement/customer_register.html', params)


def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    params = {
        'form': CustomerEditForm(instance=customer),
        'customer': customer,
    }
    if request.method == 'POST':
        form = CustomerEditForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f'得意先ID:「{customer.id}」、得意先名:「{customer.name}」を更新しました。')
            return redirect('customer-manage')
    return render(request, 'business_management/SalesAssistSystem/CustomerManagement/customer_edit.html', params)


def customer_delete(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, id=customer_id)
        deleted_customer_id = customer.id
        deleted_customer_name = customer.name
        customer.delete()
        messages.error(request, f'得意先ID:「{deleted_customer_id}」、得意先名:「{deleted_customer_name}」を削除しました。')
    return redirect('customer-manage')
