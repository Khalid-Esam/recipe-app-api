"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,  # for auth sys.
    BaseUserManager,
    PermissionsMixin,  # for permissions and fields.
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        user = self.model(email=self.normalize_email(email),
                            **extra_fields)  # define new object of User class.
        user.set_password(password)  # hashing the password.
        user.save(using=self._db)  # if using multiple DB.

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # assign usermanager

    USERNAME_FIELD = 'email'  # auth field.
