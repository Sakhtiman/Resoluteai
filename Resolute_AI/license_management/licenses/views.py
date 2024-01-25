# licenses/views.py
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import uuid
from .models import License
from datetime import timedelta
from .models import CustomUser
# from django.contrib.auth.decorators import user_passes_test
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def generate_license(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')

        # Fetch or create a license for the given client name
        license, created = License.objects.get_or_create(
            client_name=client_name,
            defaults={'expiration_date': timezone.now() + timedelta(days=30)}
        )

        return render(request, 'license.html', {'license_key': str(license.id), 'expiration_date': license.expiration_date.isoformat()})

    # Handle GET requests, you can redirect or render a different template if needed
    return render(request, 'license.html', {'license_key': None, 'expiration_date': None})
@csrf_exempt
def validate_license(request):
    if request.method == 'POST':
        license_key = request.POST.get('license_key')

        try:
            license = License.objects.get(id=uuid.UUID(license_key), is_active=True, expiration_date__gt=timezone.now())
            return render(request, 'validate_license.html', {'valid': True})
        except License.DoesNotExist:
            return render(request, 'validate_license.html', {'valid': False})
    else:
        # Handle GET requests, you can redirect or render a different template if needed
        return render(request, 'validate_license.html', {'valid': None})

def dashboard(request):
    license_count = License.objects.count()
    user_count = CustomUser.objects.count()

    context = {
        'license_count': license_count,
        'user_count': user_count,
    }

    return render(request, 'dashboard.html', context)