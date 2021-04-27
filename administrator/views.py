from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from administrator.models import Company
from .forms import newCompanyForm, newTeamForm


@login_required
def homePage(request):
    allCompanies = Company.objects.all()
    context = {'allCompanies': allCompanies}
    return render(request, 'administrator/homePage.html', context)


@login_required
def addCompany(request):
    if request.method == "POST":
        form = newCompanyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = newCompanyForm
    context = {'form': form}
    return render(request, 'administrator/addCompany.html', context)


@login_required
def addTeam(request):
    if request.method == "POST":
        form = newTeamForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = newTeamForm
    context = {'form': form}
    return render(request, 'administrator/addTeam.html', context)
