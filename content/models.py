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
