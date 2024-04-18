from django.db import models

# Create your models here.
class User(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=70)
    useremail=models.EmailField(max_length=70)
    userpass=models.CharField(max_length=70)