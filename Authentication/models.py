from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings
from datetime import datetime,timedelta
# Create your models here.

class MyUserManager(UserManager):
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        
        if not username:
            raise ValueError("The given username must be set")

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
   
    email = models.EmailField(_("email address"), blank=False,unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    wallet_address=models.CharField("Wallet Address",max_length=1000,unique=True)
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    email_verified= models.BooleanField(
        _("email_verified"),
        default=False,
        help_text=_(
            "Designates whether this users email is verfied. "
        ),
    )

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    @property
    def token(self):
        token=jwt.encode(
            {'username':self.username,'wallet_address':self.wallet_address},
            settings.SECRET_KEY,
            algorithm='HS256')
        
        return token