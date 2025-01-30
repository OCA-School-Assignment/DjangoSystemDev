from ..models import Production
from ..forms import ProductionSearchForm
from ..forms import ProductionRegisterForm, ProductionEditForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.utils import IntegrityError


def production_management(request):
    return render(request, 'business_management/ProductManagementSystem/ProductionManagement/selection.html')

class ProductionListView(ListView):
    model = Production
    template_name = 'business_management/ProductManagementSystem/ProductionManagement/production_management.html'
    context_object_name = 'productions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductionSearchForm()
        context['completed'] = self.request.GET.get('completed', '')
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')

        # queryset = queryset.prefetch_related(
        #     Prefetch('order_set', queryset=Order.objects.only('id', 'production', 'order_date', 'item_id').select_related('item'))
        # )
        if self.request.GET.get('completed') == 'true':
            queryset = queryset.filter(completion_date__isnull=False)

        query = self.request.GET.get('query', None)

        if query:
            try:
                queryset = queryset.filter(id=query)
                print(queryset)
            except ValueError:
                messages.error(self.request, '製造IDは整数で入力してください。')

        if self.request.GET.get('completed'):
            queryset = queryset.filter(completion_date__isnull=False)

        return queryset
    
def production_register(request):
    params = {
        'form': ProductionRegisterForm()
    }
    if request.method == 'POST':
        form = ProductionRegisterForm(request.POST)
        if form.is_valid():
            try:
                production = form.save(commit=False)

                if not form.cleaned_data['completion_date']:
                    production.completion_date = None
                
                production.save()
                messages.success(request, f'製造ID:「{production.id}」を登録しました。')
            except IntegrityError:
                messages.error(request, 'その受注IDに対する製造は既に登録されています。')
            return redirect('production-register')
    return render(request, 'business_management/ProductManagementSystem/ProductionManagement/production_register.html', params)
    
def production_edit(request, production_id):
    production = get_object_or_404(Production, id=production_id)
    params = {
        'form': ProductionEditForm(instance=production),
        'production': production,
    }
    if request.method == 'POST':
        form = ProductionEditForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            messages.success(request, f'製造ID:「{production.id}」を更新しました。')
            return redirect('production-manage')
    return render(request, 'business_management/ProductManagementSystem/ProductionManagement/production_edit.html', params)
    
def production_delete(request, production_id):
    if request.method == 'POST':
        production = get_object_or_404(Production, id=production_id)
        deleted_production_id = production.id
        production.delete()
        messages.error(request, f'製造ID:「{deleted_production_id}」を削除しました。')
        return redirect('production-manage')
    return redirect('production-manage')