from django.urls import path

from . import views


urlpatterns = [
    path("welcome", views.welcome_view),
    path('categories/', views.category_list, name='category_list'),
    path('locations/', views.location_list, name='location_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:pk>/', views.device_detail, name='device_detail'),
    path('devices/<int:pk>/edit/', views.device_edit, name='device_edit'),
    path('devices/<int:pk>/delete/', views.device_delete, name='device_delete'),
    path('devices/category/<int:category_id>/', views.devices_by_category, name='devices_by_category'),
    path('devices/employee/<int:employee_id>/', views.devices_by_employee, name='devices_by_employee'),
]