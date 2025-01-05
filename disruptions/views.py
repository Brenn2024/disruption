from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy 

from .models import Disruption 

class DisruptionListView(ListView): 
    model = Disruption 
    template_name = "disruption_list.html" 

class DisruptionDetailView(DetailView):  
    model = Disruption
    template_name = "disruption_detail.html" 
class DisruptionUpdateView(UpdateView):  
    model = Disruption
    fields = ( 
    "description", 
    "category", 
    "section",
    "lotnum",
    "time",
    ) 
    template_name = "disruption_edit.html" 
class DisruptionDeleteView(DeleteView):  
    model = Disruption 
    template_name = "disruption_delete.html" 
    success_url = reverse_lazy("disruption_list")

class DisruptionCreateView(CreateView): 
    model = Disruption
    template_name = "disruption_new.html" 
    fields = ( 
    "description", 
    "category", 
    "section",
    "lotnum",
    "time",
    "author",
    )