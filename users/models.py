from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Please provide user email'))
        email = self.normalize_email(email)
        user = self.model(email=email , **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'Superuser')
        if extra_fields.get('is_staff') != True:
            raise ValueError(_('Please set is_staff=True'))
        if extra_fields.get('is_superuser') != True:
            raise ValueError(_('Please set is_superuser=True'))
        return self.create_user(email, password, **extra_fields)

    def create_doctor(self, email, password, **extra_fields):
        extra_fields.setdefault('user_type', 'Doctor')
        if extra_fields.get('user_type') != 'Doctor':
            raise ValueError(_('Please set user_type=Doctor'))
        return self.create_user(email, password, **extra_fields)

    def create_patient(self, email, password, **extra_fields):
        extra_fields.setdefault('user_type', 'Patient')
        if extra_fields.get('user_type') != 'Patient':
            raise ValueError(_('Please set user_type=Patient'))

        

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Superuser','Superuser'),
    )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('Username'),
        max_length=150,
         validators=[username_validator],
        blank=True,
        null=True
    )
    email = models.EmailField(_('Email'), unique=True, blank=False, null=False)
    user_type = models.CharField(_('User Type'), max_length=20 , blank=True, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
