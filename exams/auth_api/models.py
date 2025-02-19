from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Менеджер пользователей"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        if password and len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """Кастомная модель пользователя без прав доступа"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    last_login = None

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "users"
