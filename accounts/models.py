from distutils.command import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class CustomUser(AbstractUser):
    email = models.EmailField(_("Email"), unique=True, max_length=75)
    about = models.CharField(max_length=255, default="I have nothing to say...")
    user_image = models.ImageField('Your image', upload_to ="user_img/", max_length=125, null=True, blank=True)

    def get_absolute_url(self):
        """Redirects me to the login page after a user register"""
        return reverse('accounts:login')
