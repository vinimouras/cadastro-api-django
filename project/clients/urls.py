from django.urls import path
from .views import (
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailView
)

urlpatterns = [
    path('clients/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:id>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:id>/delete/', ClientDeleteView.as_view(), name='clients-delete'),
]