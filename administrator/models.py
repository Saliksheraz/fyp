from django.contrib.auth.models import User
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
    head = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    loc_name = models.CharField(max_length=200, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now=True, null=True)
    datetime = models.DateTimeField(null=True, blank=True)
    desc = models.TextField(verbose_name="Description", null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    accuracy = models.CharField(max_length=50, null=True)
    picture = models.ImageField(null=True, blank=True)
    feedback = models.CharField(max_length=200, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    status_choice = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=100, choices=status_choice, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "AttendanceObj of " + str(self.task)


class Reports(models.Model):
    task = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    accuracy = models.CharField(max_length=50, null=True)
    picture = models.ImageField(null=True, blank=True)
    feedback = models.CharField(max_length=200, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    status_choice = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=100, choices=status_choice, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "ReportsObj of " + str(self.task)
