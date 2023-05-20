from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    customer_groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this customer belongs to. A customer will get all permissions granted to each of their groups.'),
        related_name='customer_users',
        related_query_name='customer_user',
    )
    customer_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this customer.'),
        related_name='customer_users',
        related_query_name='customer_user',
    )


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='owner_profile')
    username  = models.CharField(_('username'), max_length=30, blank=True)
    password = models.CharField(_('password'), max_length=128, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    photo =models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    id_number = models.CharField(_('id number'), max_length=20, blank=True)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
