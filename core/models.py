from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to set to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to set to is_superuser=True.'
            )
        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(
                _('You must provide an email adress')
            )
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
            _('email address'), unique=True
        )
    user_name = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
        
    about = models.TextField(
            _('about'), max_length=500, blank=True
        )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


class Device(models.Model):

    class DeviceTypes(models.TextChoices):
        ULTRASONIC = "SON", "Ultrasonic"
        GASSENSOR = "GAS", "Gassensor"
        LIGHTSENSOR = "LIGHT", "Lightsensor"
        HUMIDITYSENSOR = "HUM", "HumiditySensor"
        OTHER = "OTH","Other"
        
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    type = models.CharField(max_length=5,choices=DeviceTypes.choices, blank=False, null=False)
    reference = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(max_length=1500)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"DEVICE {self.id}"