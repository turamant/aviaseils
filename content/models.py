from django.urls import reverse


from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'pk': self.pk})


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.name


class SeatClass(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'seat'

    def __str__(self):
        return self.name


class AirPlane(models.Model):
    model = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    number_of_passengers = models.PositiveIntegerField()

    class Meta:
        db_table = 'airplane'

    def __str__(self):
        return self.model


class Flight(models.Model):
    number_flight = models.CharField(max_length=4)
    airplane = models.ForeignKey(AirPlane,
                                 on_delete=models.CASCADE,
                                 related_name='flights',
                                 verbose_name='самолёт',
                                 )
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='flights',
                                verbose_name='компания')
    departure_city = models.ForeignKey(City,
                                     on_delete=models.CASCADE,
                                     related_name='flights_dep',
                                     verbose_name='город отправления',
                                     )
    arrival_city = models.ForeignKey(City,
                                     on_delete=models.CASCADE,
                                     related_name='flights_arr',
                                     verbose_name='город прибытия',
                                     )
    data_departure = models.DateField(verbose_name='дата отправления')
    time_departure = models.TimeField(verbose_name='время отправления')
    data_arrive = models.DateTimeField(verbose_name='дата и время прибытия')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'flight'
        ordering = ('data_departure',)

    def __str__(self):
        return self.number_flight

    class Client(models.Model):
        last_name = models.CharField(max_length=100, verbose_name='Фамилия')
        first_name = models.CharField(max_length=100, verbose_name='Имя')
        passport_number = models.CharField(max_length=13, verbose_name='Номер паспорта')
        email = models.CharField(max_length=100, verbose_name='Электронный ящик')
        phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')







