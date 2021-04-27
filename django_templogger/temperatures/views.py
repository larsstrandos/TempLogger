from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View

from .models import Temp

from django.views.generic import (
    DetailView
)

class TempDetailView(View):
    template_name = 'temps/temp_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {
        }
        if id is not None:
            # Gets a list of ALL temps with the right sensor_ID
            obj_list = get_list_or_404(Temp.objects.order_by('-created_date'), sensor_id=id)
            context['object_list'] = obj_list
            

            # Get the most current Temp form the right sensor_ID
        return render(request, self.template_name, context)

    #def get_object(self):
     #   id_ = self.kwargs.get("id")
      #  return get_object_or_404(Temp, id=id_)
