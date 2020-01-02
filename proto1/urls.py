from django.urls import path
from .views import EventListView, EventRegisterView, EventDetailView

app_name = 'proto1'

urlpatterns = [
    path('event/list', EventListView.as_view(), name='event_list'),
    path('event/detail/<int:event_id>', EventDetailView.as_view(), name='event_detail'),
    path('event/register', EventRegisterView.as_view(), name='event_register'),
]
