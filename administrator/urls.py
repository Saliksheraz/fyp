from django.urls import path
from . import views, ajax

urlpatterns = [
    path('adminPanelAjax/', ajax.adminPanelAjax, name='adminPanelAjax'),
]
