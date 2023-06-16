from django.urls import path

from content import views

urlpatterns = [
    path('avia/', views.index, name='index'),
    path('flights/', views.all_flights, name='all_flights'),
    path('companies/', views.list_company, name='companies'),
    path('companies/<int:pk>/', views.get_company, name='company'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/<int:pk>/update/', views.update_company, name='update_company'),
    path('companies/<int:pk>/delete/', views.delete_company, name='delete_company'),

    path('find/', views.find_flights, name='find_flights'),
    path('find/<int:idd>/', views.find_flight_detail, name='find_flight_detail'),
    path('find-data/', views.find_flights_data, name='find_flights_data'),

    path('flight/create/', views.create_flight, name='create_flight'),


    path('airplanes/', views.get_airplanes, name='airplanes'),
    path('airplane-flights/<int:pk>/', views.airplane_flights, name='airplane_flights'),
]