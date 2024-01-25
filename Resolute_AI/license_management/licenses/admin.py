# licenses/admin.py
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from .models import CustomUser, License

class CustomAdmin(admin.AdminSite):
    site_header = 'Custom Admin Dashboard'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='custom_dashboard'),
            path('usage_statistics/', self.admin_view(self.usage_statistics_view), name='usage_statistics'),
            path('generate_reports/', self.admin_view(self.generate_reports_view), name='generate_reports'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Custom logic for the dashboard view
        total_users = CustomUser.objects.count()
        total_licenses = License.objects.count()

        context = {
            'total_users': total_users,
            'total_licenses': total_licenses,
        }
        return TemplateResponse(request, 'admin/dashboard.html', context)

    def usage_statistics_view(self, request):
        # Custom logic for the usage statistics view
        # Example: Fetch data from the database and calculate statistics
        # ...

        context = {
            # Add data for usage statistics...
        }
        return TemplateResponse(request, 'admin/usage_statistics.html', context)

    def generate_reports_view(self, request):
        # Custom logic for the generate reports view
        # Example: Generate reports or fetch existing reports
        # ...

        context = {
            # Add data or information for reports...
        }
        return TemplateResponse(request, 'admin/generate_reports.html', context)

custom_admin_site = CustomAdmin(name='customadmin')

# Register models with the custom admin site
custom_admin_site.register(CustomUser)
custom_admin_site.register(License)

admin.site.register(CustomUser)
