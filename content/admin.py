from django.contrib import admin

from content.models import Company, City


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