from django.db import models
from django.contrib.auth.models import User
from administrator.models import Company, Team


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    level = models.CharField(max_length=50, default='team_member', null=True)
    levelInt = models.IntegerField(default=10, null=True)

    phone = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=300, null=True)
    gender = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    firstName = models.CharField(max_length=30, null=True)
    secondName = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=30, null=True)
    facebook = models.CharField(max_length=30, null=True)
    insta = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)
