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
    
    def _create_user(self, wallet_address, password, **extra_fields):
        """
        Create and save a user with the given wallet_address,  and password.
        """
        
        if not wallet_address:
            raise ValueError("The given wallet_address must be set")

     
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        wallet_address = GlobalUserModel.normalize_username(wallet_address)
        user = self.model(wallet_address=wallet_address, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, wallet_address,  password="Pass@123", **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(wallet_address,  password, **extra_fields)

    def create_superuser(self, wallet_address,  password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(wallet_address,  password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    
    username_validator = UnicodeUsernameValidator()
    wallet_address = models.CharField(
        _("wallet_address"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that wallet_address already exists."),
        },
        primary_key=True
    )
   
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = "wallet_address"
    

    @property
    def token(self):
        token=jwt.encode(
            {'wallet_address':self.wallet_address},
            settings.SECRET_KEY,
            algorithm='HS256')
        
        return token