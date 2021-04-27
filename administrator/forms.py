from django import forms
from .models import Company, Team


class newCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class newTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
