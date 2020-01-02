from django.urls import path
from .views import EventFilterView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView


urlpatterns = [
    path('',  EventFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', EventDetailView.as_view(), name='detail'),
    path('create/', EventCreateView.as_view(), name='create'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='delete'),
]
