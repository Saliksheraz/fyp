from django import forms
from .models import Company, Team, Tasks, Attendance, Reports


class newCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class newTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class newTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = {'createdBy'}


class attendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = {'dateCreation', 'user'}


class reportSubmissionForm(forms.ModelForm):
    class Meta:
        model = Reports
        exclude = {'dateCreation', 'user'}
