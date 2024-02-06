from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    


    def __str__(self):
        return self.username
