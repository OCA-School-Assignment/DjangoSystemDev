from ..models import Employee, Items
from ..forms import ProductSearchForm, ProductRegisterForm, ProductEditForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.utils import IntegrityError
from django.http import HttpResponseForbidden


def product_management(request):
    return render(request, 'business_management/ProductManagementSystem/ProductManagement/selection.html')


class ProductListView(ListView):
    model = Items
    template_name = 'business_management/ProductManagementSystem/ProductManagement/product_management.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_type = self.request.GET.get('search_type', '')
        query = self.request.GET.get('query', '')
        
        if search_type == 'id' and query:
            # queryset = queryset.filter(id=query)
            queryset = queryset.filter(id__icontains=query)
        elif search_type == 'name' and query:
            queryset = queryset.filter(name__icontains=query)
        
        return queryset


def product_register(request):  
    params = {
        'form': ProductRegisterForm()
    }
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            product_name = form.cleaned_data['product_name']
            price = form.cleaned_data['price']
            try:
                product = Items.objects.create(id=product_id, name=product_name, price=price)
                product.save()
                messages.success(request, f'製品ID:「{product.id}」、製品名:「{product.name}」、価格:「{product.price}」を登録しました。')
                return redirect('/product-management/register')
            except IntegrityError:
                messages.error(request, '製品IDが既に登録されています。')
                return redirect('/product-management/register')
    return render(request, 'business_management/ProductManagementSystem/ProductManagement/product_register.html', params)


def product_edit(request, product_id):
    product = get_object_or_404(Items, id=product_id)
    params = {
        'form': ProductEditForm(instance=product),
        'product': product,
    }
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'製品ID:「{product.id}」、製品名:「{product.name}」、価格:「{product.price}」を更新しました。')
            return redirect('product-manage')
    return render(request, 'business_management/ProductManagementSystem/ProductManagement/product_edit.html', params)


def product_delete(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Items, id=product_id)
        deleted_product_id = product.id
        deleted_product_name = product.name
        product.delete()
        messages.error(request, f'製品ID:「{deleted_product_id}」、製品名:「{deleted_product_name}」、、価格:「{product.price}」を削除しました。')
        return redirect('product-manage')
    return redirect('product-manage')
