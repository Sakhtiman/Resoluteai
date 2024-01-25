# licenses/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    
    ROLES = [
        (ADMIN, 'Administrator'),
        (MANAGER, 'Manager'),
    ]

    role = models.CharField(max_length=20, choices=ROLES)

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='user permissions',
    )
