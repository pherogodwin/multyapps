from django.urls import path
from . import views
app_name = "weather"

urlpatterns = [
    # path('home/', views.home, name='home'),

    path('weather-check/', views.weather_view, name='weather_view'),
    # path('add/', views.add_task, name='add_task'),
    # path('all/', views.all_tasks, name='all_tasks'),

    # path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
