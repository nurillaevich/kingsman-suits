
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_('Enter a valid email address.'))

    def create_user(self, email, name, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_('Please enter your email address.'))
        if not name:
            raise ValidationError(_('Please enter your first name.'))

        user = self.model(email=email, name=name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError(_('Staff fields must have `is_staff`.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValidationError(_('Superuser fields must have `is_superuser`.'))
        user = self.create_user(email, name, **extra_fields)
        user.save(using=self._db)
        return user
