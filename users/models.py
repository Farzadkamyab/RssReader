from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import re
from main.models import BaseModel
from .managers import UserManager

# Create your models here.
PHONE_REGEX_PATTERN = r"(((\+|00)(98))|0)?(?P<operator>9\d{2})-?(?P<middle3>\d{3})-?(?P<last4>\d{4})"

def phone_validator(phone:str):
    if not (matched := re.fullmatch(PHONE_REGEX_PATTERN, phone.strip())):
        raise ValidationError("Invalid phone number")
    return matched

class PhoneNumberField(models.CharField):
    def get_prep_value(self, value):
        if value is None:
            return value

        try:
            regex = phone_validator(value)
        except ValidationError:
            raise

        phone_parts = regex.groupdict()
        phone = phone_parts["operator"]+phone_parts["middle3"]+phone_parts["last4"]
        return phone

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone = PhoneNumberField(validators=[phone_validator], unique=True, max_length=20)

    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone}"