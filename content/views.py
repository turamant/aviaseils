from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from content import services
from content.forms import CompanyForm, FindTicketForm, FindTicketDataForm, FlightForm, FlightFilterForm
from content.models import Company, Flight, AirPlane
from content.services import get_flight_with_city_and_data, get_flight_with_city


# Create your views here.


def index(request):
    return render(request, 'content/index.html')


def flight_list(request):
    flights = Flight.objects.all()
    form = FlightFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            flights = flights.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            flights = flights.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['ordering']:
            flights = flights.order_by(form.cleaned_data['ordering'])


    context = {'flights': flights,
               'form': form}
    return render(request, 'content/flight/flight_list.html', context)


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    context = {'flight': flight}
    return render(request, 'content/flight/flight_detail.html', context)


def create_flight(request):
    form = FlightForm()
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'content/flight/flight_create.html', context)


def update_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    form = FlightForm(instance=flight)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'content/flight/flight_update.html', context)


def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        flight.delete()
        return redirect('/')
    return render(request, 'content/flight/flight_delete.html', {'flight': flight})


def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'content/company/company_list.html', context)


def company_detail(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {'company': company}
    return render(request, 'content/company/company_detail.html', context)


def create_company(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'content/company/company_create.html', context)


def update_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'content/company/company_update.html', context)


def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('/')
    return render(request, 'content/company/company_delete.html', {'company': company})


def find_flights(request):
    """ Поиск по городам вылета и прилета"""
    if request.method == 'POST':
        city1 = request.POST.get('city1')
        city2 = request.POST.get('city2')
        flights = get_flight_with_city(city1, city2)
        context = {'row': flights}
        return render(request, 'content/flight/result_find_flights.html', context)

    else:
        form = FindTicketForm()
        context = {'form': form}
        return render(request, 'content/flight/find_flights.html', context)


def find_flights_data(request):
    """ Поиск по городам вылета и прилета"""
    if request.method == 'POST':
        city1 = request.POST.get('city1')
        city2 = request.POST.get('city2')
        data_depart = request.POST.get('data_depart')
        flights = get_flight_with_city_and_data(city1, city2, data_depart)
        context = {'row': flights}
        return render(request, 'content/flight/result_find_flights_data.html', context)
    else:
        form = FindTicketDataForm()
        context = {'form': form}
        return render(request, 'content/flight/find_flights_data.html', context)





def get_airplanes(request):
    airplanes = AirPlane.objects.all()
    context ={
        'airplanes': airplanes
    }
    return render(request, 'content/airplane/airplanes.html', context)


def airplane_flights(request, pk):
    airplane = get_object_or_404(AirPlane, pk=pk)
    flights = services.get_airplane_flights(airplane)
    return render(request, 'content/airplane/airplane_flights.html', {
        'airplane': airplane,
        'flights': flights,
    })


