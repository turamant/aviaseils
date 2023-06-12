from django.urls import path

from content import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies/', views.list_company, name='companies'),
    path('companies/<int:pk>/', views.get_company, name='company'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/<int:pk>/update/', views.update_company, name='update_company'),
    path('companies/<int:pk>/delete/', views.delete_company, name='delete_company')

]