from django.contrib.auth.forms import UserCreationForm
from django import forms

#################### Django User Registration Form to Register a new User ###########
from administrator.models import Company, Team


class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=100)
    secondName = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=300)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('ratherNotSay', 'Rather Not Say')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    picture = forms.ImageField(required=False)
    mobile = forms.CharField(max_length=100)
    website = forms.CharField(max_length=100, required=False)
    facebook = forms.CharField(max_length=100, required=False)
    insta = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    level_choices = ()
    level = forms.ChoiceField(choices=level_choices, required=False)
    company = forms.ModelChoiceField(queryset=Company.objects.none(), required=False, label='Company')
    team = forms.ModelChoiceField(queryset=Team.objects.none(), required=False, label='Company')

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        userLevelCheck(self, request)


def userLevelCheck(self, request):
    level_choices = ()
    if request.user.is_superuser:
        level_choices += ('owner', 'Owner'), ('ceo', 'CEO'), ('manager', 'Manager'), (
            'team_member', 'Team Member')
    elif request.user.profile.level == 'owner':
        level_choices += ('ceo', 'CEO'), ('manager', 'Manager'), (
            'team_member', 'Team Member')
    elif request.user.profile.level == 'ceo':
        level_choices += ('manager', 'Manager'), ('team_member', 'Team Member')
    elif request.user.profile.level == 'manager':
        level_choices += ('team_member', 'Team Member')
    self.fields['level'].choices = level_choices
    self.fields['team'].queryset = Team.objects.all()
    if request.user.profile.level == 'owner' or request.user.is_superuser:
        self.fields['company'].queryset = Company.objects.all()
    elif request.user.profile.level == 'ceo':
        self.fields['company'].queryset = Company.objects.all()
    elif request.user.profile.level == 'manager':
        self.fields['company'].queryset = Company.objects.all()
    elif request.user.profile.level == 'team_member':
        self.fields['company'].queryset = Company.objects.all()
