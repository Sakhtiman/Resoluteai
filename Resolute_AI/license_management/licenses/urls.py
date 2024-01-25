# licenses/urls.py
from django.urls import path, include
from .views import generate_license, validate_license, home,dashboard
from .admin import custom_admin_site


urlpatterns = [
    path('generate_license/', generate_license, name='generate_license'),
    path('validate_license/', validate_license, name='validate_license'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('admined/', custom_admin_site.urls),  # Include custom admin URLs

]
