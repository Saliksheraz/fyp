from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from administrator.models import Company, Team, Tasks
from .forms import newCompanyForm, newTeamForm, newTaskForm, attendanceForm


@login_required
def homePage(request):
    allCompanies = Company.objects.all()
    allTeams = Team.objects.all()
    context = {'allCompanies': allCompanies, 'allTeams': allTeams}
    return render(request, 'administrator/homePage.html', context)


@login_required
def addCompany(request):
    if request.method == "POST":
        form = newCompanyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, form.errors)
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
            messages.warning(request, form.errors)
    form = newTeamForm
    context = {'form': form}
    return render(request, 'administrator/addTeam.html', context)


@login_required
def createTask(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, form.errors)
    form = newTaskForm
    context = {'form': form}
    return render(request, 'administrator/createTask.html', context)


@login_required
def viewTasks(request):
    allTasks = Tasks.objects.all()
    context = {'allTasks': allTasks}
    return render(request, 'administrator/viewTasks.html', context)


@login_required
def attendance(request, pk):
    object = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        form = attendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('homePage')
        else:
            messages.warning(request, form.errors)
    form = attendanceForm
    context = {'object': object, 'form': form}
    return render(request, 'administrator/attendance.html', context)
