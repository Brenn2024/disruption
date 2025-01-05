from django.urls import path 
from .views import DisruptionListView,DisruptionDetailView,DisruptionUpdateView,DisruptionDeleteView,DisruptionCreateView
urlpatterns = [
 path("<int:pk>/", DisruptionDetailView.as_view(), 
    name="disruption_detail"),  
path("<int:pk>/edit/", DisruptionUpdateView.as_view(), 
    name="disruption_edit"), 
path("<int:pk>/delete/", DisruptionDeleteView.as_view(), 
    name="disruption_delete"),
path("new/", DisruptionCreateView.as_view(), name="article_new"), 
path("", DisruptionListView.as_view(), name="disruption_list"),
]