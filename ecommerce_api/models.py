from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
import os
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

# User model


class User(AbstractBaseUser):
    
    email = models.EmailField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="AD01")

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    GENDER_CHOICES = (
        ("FEMME", "Femme"),
        ("HOMME", "Homme"),
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES)
    birthday =models.DateField
    tel= models.CharField(max_length=25, blank=True)

    image = models.ImageField(
        upload_to="uploads/avatars",
        blank=True,
        null=True,
    )
    addres = models.CharField(max_length=150, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=255, blank=True)
    edited_by = models.CharField(max_length=255, blank=True)
    date_modification = models.DateTimeField(
        auto_now=True, null=True, auto_now_add=False)

    objects = UserManager()

    USERNAME_FIELD = "code"

    def save(self, *args, **kwargs):

        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.password = make_password(self.password)

        # Generate the code if it's a new user
        if not self.pk:

            if isinstance(self, Seller):
                prefix = 'VD'
            elif isinstance(self, Buyer):
                prefix = 'AC'
            else:
                prefix = 'AD'

            max_code = User.objects.filter(code__startswith=prefix).order_by(
                '-code').values_list('code', flat=True).first()
            if max_code:
                sequence_number = int(max_code[2:]) + 1
            else:
                sequence_number = 1
            self.code = f"{prefix}{sequence_number:02d}"

        # image

        if self.id:

            old_instance = User.objects.get(id=self.id)
            if self.image != old_instance.image:
                if (
                    old_instance.image
                ):
                    os.remove(old_instance.image.path)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


# Seller model
class Seller(User):

    etat = models.BooleanField(default=True)

    def __str__(self):
        return self.email

# Buyer model
class Buyer(User):
    etat = models.BooleanField(default=True)

    def __str__(self):
        return self.email

# Manager model
class Manager(User):

    ROLE_CHOICES = (

        ("ADMIN", "Admin"),
        ("RESPO", "Respo"),
        ("MASTER", "Master"),
        ("SUPERADMIN", "Superadmin"),

    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="ADMIN")
    etat = models.BooleanField(default=True)

    def __str__(self):

        return self.email