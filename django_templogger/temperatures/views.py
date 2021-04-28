from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View

from .models import Temp

class TempDetailView(View):
    template_name = 'temps/temp_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {
            'loop_times': range(1, 15)
        }
        if id is not None:
            # Gets a list of ALL temps with the selected sensor_ID and order by created date
            obj_list = get_list_or_404(Temp.objects.order_by('-created_date'), sensor_id=id)
            context['object_list'] = obj_list
            
        return render(request, self.template_name, context)
