from django.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Company", null=True, unique=True)
    country = CountryField(blank=True, null=True)
    weblink = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    google_pin = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    postalcode = models.CharField(max_length=50, verbose_name='Postal Code', blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cell Phone 1")
    phone2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cell Phone 2")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200, verbose_name="Team", null=True)
    desc = models.TextField(verbose_name="Description", null=True)
    head = models.CharField(max_length=200, verbose_name="Head", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
