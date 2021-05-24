from django import forms
from .models import Company, Team, Tasks, Attendance


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
        fields = '__all__'


class attendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = {'datetime', 'user'}
