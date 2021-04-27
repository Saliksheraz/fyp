from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from administrator import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from users.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('register/', user_views.register, name='register'),
    url(r'profile/', profile, name='profile'),
    url(r'addCompany/', views.addCompany, name='addCompany'),
    url(r'addTeam/', views.addTeam, name='addTeam'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
