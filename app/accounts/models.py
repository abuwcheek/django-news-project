from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.


class User(AbstractUser):
    phone=models.CharField(max_length=15, null=True, blank=True)
    avatar=models.ImageField(upload_to='user_avatar', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'heic'))])


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def hashing_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    
    def save(self, *args, **kwargs):
        self.hashing_password()
        return super().save(*args, **kwargs)