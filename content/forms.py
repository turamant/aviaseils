import datetime

from django.forms import ModelForm
from .models import Company, Flight, City, AirPlane

from django import forms


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "slug",
            "address",
            "email",
        ]


class FindTicketForm(forms.Form):
    city1 = forms.CharField()
    city2 = forms.CharField()


class FindTicketDataForm(forms.Form):
    city1 = forms.CharField()
    city2 = forms.CharField()
    data_depart = forms.DateTimeField()


class Airplane:
    pass


class FlightForm(forms.ModelForm):
    airplane = forms.ModelChoiceField(queryset=AirPlane.objects.all())
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    departure_city = forms.ModelChoiceField(queryset=City.objects.all())
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all())

    class Meta:
        model = Flight
        fields = '__all__'



