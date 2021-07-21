from django.urls import path
from .views import LeadCreateView, LeadListView, LeadClaimView

urlpatterns = [
    path('create/', LeadCreateView.as_view(), name='create'),
    path('list/', LeadListView.as_view(), name='list'),
    path('claim/', LeadClaimView.as_view(), name='claim')
]
