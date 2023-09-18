from django.db import models

class UserLogin(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)


class UserRegister(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Log_id=models.ForeignKey(UserLogin,on_delete=models.CASCADE)


