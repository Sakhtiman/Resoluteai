"""license_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# licenses/urls.py
# license_management/urls.py
# license_management/urls.py
from django.contrib import admin
from django.urls import path, include
from licenses.admin import custom_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),  # Include the default admin URLs
    path('customadmin/', custom_admin_site.urls),  # Include the custom admin URLs
    path('licenses/', include('licenses.urls')),  # Assuming your app is named 'licenses'
    # Add a pattern for the root path
    path('', include('licenses.urls')),  # You can replace 'licenses.urls' with your actual app's URL configuration
]



