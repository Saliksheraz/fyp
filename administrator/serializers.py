from django.contrib.auth.models import User
from rest_framework import serializers
from administrator.models import Company, Team, Tasks, Attendance, Reports


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class ReportsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'
