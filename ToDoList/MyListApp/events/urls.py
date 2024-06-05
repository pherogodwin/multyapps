# events/urls.py

from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('book/<int:seat_id>/', views.book_ticket, name='book_ticket'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
