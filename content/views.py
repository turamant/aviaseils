from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from content import services
from content.forms import CompanyForm, FindTicketForm, FindTicketDataForm, FlightForm
from content.models import Company, Flight, AirPlane
from content.services import get_flight_with_city_and_data, get_flight_with_city


# Create your views here.


def index(request):
    return render(request, 'content/index.html')


def list_company(request):
    companies = Company.objects.all()
    #companies = Company.objects.raw('SELECT * FROM company')
    context = {'companies': companies}
    return render(request, 'content/list_company.html', context)


def get_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {'company': company}
    return render(request, 'content/company.html', context)


def create_company(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "content/company_create.html", context)


def update_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    form = CompanyForm(instance=company)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form,
    }
    return render(request, "content/company_update.html", context)


def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method == "POST":
        company.delete()
        return redirect("/")
    return render(request, "content/company_delete.html", {'company': company})


def find_ticket(request):
    """ Поиск по городам вылета и прилета"""
    if request.method == "POST":
        city1 = request.POST.get("city1")
        city2 = request.POST.get("city2")
        flights = get_flight_with_city(city1, city2)
        context = {'row': flights}
        return render(request, "content/result_find_ticket.html", context)

    else:
        form = FindTicketForm()
        context = {'form': form}
        return render(request, "content/find_ticket.html", context)


def find_ticket_data(request):
    """ Поиск по городам вылета и прилета"""
    if request.method == "POST":
        city1 = request.POST.get("city1")
        city2 = request.POST.get("city2")
        data_depart = request.POST.get("data_depart")
        flights = get_flight_with_city_and_data(city1, city2, data_depart)
        context = {'row': flights}
        return render(request, "content/result_find_ticket_data.html", context)
    else:
        form = FindTicketDataForm()
        context = {'form': form}
        return render(request, "content/find_ticket_data.html", context)


def find_ticket_detail(request, idd):
    ticket = get_object_or_404(Flight, id=idd)
    context = {'ticket': ticket}
    return render(request, 'content/result_find_ticket_detail.html', context)


def create_flight(request):
    form = FlightForm()
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "content/flight_create.html", context)


def get_airplanes(request):
    airplanes = AirPlane.objects.all()
    context ={
        "airplanes": airplanes
    }
    return render(request, 'content/airplanes.html', context)

def airplane_flights(request, pk):
    airplane = get_object_or_404(AirPlane, pk=pk)
    flights = services.get_airplane_flights(airplane)
    return render(request, 'content/airplane_flights.html', {
        'airplane': airplane,
        'flights': flights,
    })
