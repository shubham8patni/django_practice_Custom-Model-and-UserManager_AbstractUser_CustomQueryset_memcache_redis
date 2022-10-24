from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

# Create your manager here.
class MyManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(
        #     self.model._meta.app_label, self.model._meta.object_name
        # )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):  # password : ramiro900
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class maleQuery(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='male')
class femaleQuery(models.Manager):
    def get_queryset(self):    
        return super().get_queryset().filter(gender='female')


# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    ]
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] ## if making a field like "email" as username then remove it from required fields 
    email = models.EmailField(unique=True)
    username = models.CharField(("username"),max_length=150, unique=False, help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."))
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES, null = False, default = GENDER_CHOICES[2][0])
    birthday = models.DateField(null = True)

    objects = MyManager()
    male = maleQuery()
    female = femaleQuery()

    def __str__(self):
        return self.email