from ..models import Stock
from ..forms import StockSearchForm
from django.views.generic import ListView

class StockListView(ListView):
    model = Stock
    template_name = 'business_management/ProductManagementSystem/StockManagement/stock_management.html'
    context_object_name = 'stocks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = StockSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_type = self.request.GET.get('search_type', '')
        query = self.request.GET.get('query', '')
        
        if search_type == 'item_id' and query:
             queryset = queryset.select_related('item').filter(item_id__id__icontains=query)
        elif search_type == 'name' and query:
            queryset = queryset.select_related('item').filter(item_id__name__icontains=query)

        queryset = queryset.order_by('location')
        
        return queryset
    