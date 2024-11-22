from datetime import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser 


from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser (AbstractBaseUser ):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=255, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser , on_delete=models.CASCADE)  # Changed from username to user
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=255, blank=True)  # Use EmailField for consistency

    def __str__(self):
        return self.user.email
    

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f'Token for {self.user.email}'
    


    
