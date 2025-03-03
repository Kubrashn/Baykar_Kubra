from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps 

class Kullanici(AbstractUser):
    takim = models.ForeignKey("main.Takim", on_delete=models.SET_NULL, null=True, blank=True)  
    tc_no = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telefon_no = models.CharField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = "tc_no"
    REQUIRED_FIELDS = ["username", "telefon_no"]

    def __str__(self):
        return f"{self.username} - {self.tc_no}"
