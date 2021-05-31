from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from administrator import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from users.views import profile
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'attendances', views.AttendanceViewSet)
router.register(r'reports', views.ReportsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrator.urls')),
    path('register/', user_views.register, name='register'),
    url(r'profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
