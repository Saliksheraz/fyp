import datetime
import datedelta
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from administrator.models import Company, Team, Tasks, Reports, Attendance
from administrator.serializers import UserSerializer, CompanySerializer, TeamSerializer, TasksSerializer, \
    AttendanceSerializer, ReportsSerializer
from .forms import newCompanyForm, newTeamForm, newTaskForm, attendanceForm, reportSubmissionForm
from rest_framework import permissions


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
            messages.success(request, "Company added successfully !!!")
            return redirect('homePage')
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
            messages.success(request, "Team created successfully !!!")
            return redirect('homePage')
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
            form.instance.createdBy = request.user
            form.save()
            messages.success(request, "Task created successfully !!!")
            return redirect('viewTasks')
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
def viewAttendance(request):
    allAttendance = Attendance.objects.all()
    context = {'allAttendance': allAttendance}
    return render(request, 'administrator/viewAttendance.html', context)


@login_required
def attendanceAnalytics(request):
    today = datetime.date.today()
    current_date = str(today)
    current_year = int(current_date.split('-')[0])
    current_month = int(current_date.split('-')[1])
    current_day = int(current_date.split('-')[2])
    date = datetime.date(current_year, current_month - 1, current_day)
    list = []
    while date <= today:
        completed = Attendance.objects.filter(dateCreation__date=date, status='Completed').count()
        pending = Attendance.objects.filter(dateCreation__date=date, status='Pending').count()
        total = Attendance.objects.filter(dateCreation__date=date).count()
        list.append(attnData(total, str(date), completed, pending))
        date += datedelta.DAY
    todaysTotal = Attendance.objects.filter(dateCreation__date=current_date).count()
    todaysCompleted = Attendance.objects.filter(dateCreation__date=current_date, status='Completed').count()
    todaysPending = Attendance.objects.filter(dateCreation__date=current_date, status='Pending').count()
    todaysTotalReport = Reports.objects.filter(dateCreation__date=current_date).count()
    todaysCompletedReport = Reports.objects.filter(dateCreation__date=current_date, status='Completed').count()
    todaysPendingReport = Reports.objects.filter(dateCreation__date=current_date, status='Pending').count()

    context = {'list': list, 'todaysTotal': todaysTotal, 'todaysCompleted': todaysCompleted,
               'todaysPending': todaysPending, 'todaysTotalReport': todaysTotalReport,
               'todaysCompletedReport': todaysCompletedReport,
               'todaysPendingReport': todaysPendingReport}
    return render(request, 'administrator/attendanceAnalytics.html', context)


class attnData:
    def __init__(self, total, date, completed, pending):
        self.total = total
        self.date = date
        self.completed = completed
        self.pending = pending


@login_required
def attendance(request, pk):
    object = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        form = attendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('viewAttendance')
        else:
            messages.warning(request, form.errors)
    form = attendanceForm
    context = {'object': object, 'form': form}
    return render(request, 'administrator/attendance.html', context)


@login_required
def reportSubmit(request):
    if request.method == 'POST':
        form = reportSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('viewReports')
        else:
            messages.warning(request, form.errors)
    form = reportSubmissionForm
    context = {'form': form}
    return render(request, 'administrator/reportSubmit.html', context)


@login_required
def viewReports(request):
    allData = Reports.objects.all()
    context = {'allData': allData}
    return render(request, 'administrator/viewReports.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [permissions.IsAuthenticated]
