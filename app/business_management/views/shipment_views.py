from ..models import Stock, ShipmentLog
from ..forms import ShipmentLogSearchForm
from django.views.generic import ListView
from django.shortcuts import render

class ShipmentLogListView(ListView):
    model = ShipmentLog
    template_name = 'business_management/ProductManagementSystem/ShipmentManagement/shipment_management.html'
    context_object_name = 'shipment_logs'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ShipmentLogSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.session.get('department_name') == 'Production Management':
            queryset = queryset.filter(action='In').order_by('id')
        else:
            queryset = queryset.filter(action='Out').order_by('id')

        search_type = self.request.GET.get('search_type', '')
        query = self.request.GET.get('query', '')
        
        if search_type == 'item_id' and query:
             queryset = queryset.select_related('item').filter(item_id__id__icontains=query)
        elif search_type == 'name' and query:
            queryset = queryset.select_related('item').filter(item_id__name__icontains=query)

        queryset = queryset.order_by('location')
        
        return queryset
    
def shipment_test(request):
    shipment_all = ShipmentLog.objects.all()
    return render(request, 'business_management/ProductManagementSystem/ShipmentManagement/shipment_test.html', {'shipment_all': shipment_all})