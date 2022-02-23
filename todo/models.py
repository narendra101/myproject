from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=8)
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return self.username

