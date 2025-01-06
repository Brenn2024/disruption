from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy 

from .models import Disruption 

class DisruptionListView(LoginRequiredMixin,ListView): 
    model = Disruption 
    template_name = "disruption_list.html" 

class DisruptionDetailView(LoginRequiredMixin,DetailView):  
    model = Disruption
    template_name = "disruption_detail.html" 
class DisruptionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):  
    model = Disruption
    fields = ( 
    "description", 
    "category", 
    "section",
    "lotnum",
    "time",
    ) 
    template_name = "disruption_edit.html" 
    def test_func(self):  
        obj = self.get_object() 
        return obj.author == self.request.user 
class DisruptionDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):  
    model = Disruption 
    template_name = "disruption_delete.html" 
    success_url = reverse_lazy("disruption_list")
    def test_func(self):  
        obj = self.get_object() 
        return obj.author == self.request.user 

class DisruptionCreateView(LoginRequiredMixin,CreateView): 
    model = Disruption
    template_name = "disruption_new.html" 
    fields = ( 
    "description", 
    "category", 
    "section",
    "lotnum",
    "time",
    )
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super().form_valid(form) 