from django.urls import path

from content import views

urlpatterns = [
    path('', views.index, name='index'),

    path('flights/', views.flight_list, name='flight_list'),
    path('flights/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('flights/create/', views.create_flight, name='create_flight'),
    path('flights/<int:flight_id>/update/', views.update_flight, name='update_flight'),
    path('flights/<int:flight_id>/delete/', views.delete_flight, name='delete_flight'),

    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/<int:pk>/update/', views.update_company, name='update_company'),
    path('companies/<int:pk>/delete/', views.delete_company, name='delete_company'),

    path('find/', views.find_flights, name='find_flights'),

    path('find-data/', views.find_flights_data, name='find_flights_data'),



    path('airplanes/', views.get_airplanes, name='airplanes'),
    path('airplane-flights/<int:pk>/', views.airplane_flights, name='airplane_flights'),
]