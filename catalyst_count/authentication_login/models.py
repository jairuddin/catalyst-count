from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), max_length=150, unique=True)


    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs) 


    def validate_password(self):
        if not any(char.isdigit() for char in self.password):
            raise ValidationError(_("Password must contain at least one digit."), code='password_no_number')
        if not any(char.isupper() for char in self.password):
            raise ValidationError(_("Password must contain at least one uppercase letter."), code='password_no_upper')
        if not any(char.islower() for char in self.password):
            raise ValidationError(_("Password must contain at least one lowercase letter."), code='password_no_lower')
        if len(self.password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."), code='password_too_short')
        

    def clean_password(self):
        self.validate_password()
        return self.password
