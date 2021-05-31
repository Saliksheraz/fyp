from django.conf.urls import url
from django.urls import path
from . import views, ajax

urlpatterns = [
    path('adminPanelAjax/', ajax.adminPanelAjax, name='adminPanelAjax'),

    path('', views.homePage, name='homePage'),

    url(r'addCompany/', views.addCompany, name='addCompany'),

    url(r'addTeam/', views.addTeam, name='addTeam'),

    path('createTask/', views.createTask, name='createTask'),
    path('viewTasks/', views.viewTasks, name='viewTasks'),

    url(r'attendance/(?P<pk>[0-9]+)/$', views.attendance, name='attendance'),

    path('reportSubmit/', views.reportSubmit, name='reportSubmit'),
    path('viewReports/', views.viewReports, name='viewReports'),


]
