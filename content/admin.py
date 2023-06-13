from django.contrib import admin

from content.models import Company, City, SeatClass, AirPlane, Flight


# Register your models here.


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ('name',
                    'slug',
                    'address',
                    'email',
                    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ('name',
                    'slug',
                    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SeatClass)
class AdminSeatClass(admin.ModelAdmin):
    list_display = ('name',
                    'slug',
                    'price',
                    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AirPlane)
class AdminAirPlane(admin.ModelAdmin):
    list_display = ('model',
                    'slug',
                    'number_of_passengers',
                    )
    prepopulated_fields = {'slug': ('model',)}


@admin.register(Flight)
class AdminFlight(admin.ModelAdmin):
    list_display = ('number_flight',
                    'airplane',
                    'company',
                    'departure_city',
                    'arrival_city',
                    'data_departure',
                    'time_departure',
                    'data_arrive',
                    'price',
                    )

