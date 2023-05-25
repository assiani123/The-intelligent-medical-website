from django.db import models

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)

class D(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
class E(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100)
     dep=models.CharField(max_length=100)
     date=models.DateField()
class rdv(models.Model):
   
        id=models.AutoField(primary_key=True)
        nomm=models.CharField(max_length=100)
        nomp=models.CharField(max_length=100)
        date=models.DateField()
        Time=models.CharField(max_length=100)
        prix=models.CharField(max_length=100)
        spec=models.CharField(max_length=100)
        etat=models.CharField(max_length=100)

   

from django.contrib.auth.models import AbstractUser, Group, Permission,AbstractBaseUser




class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role= models.CharField(max_length=255)
    spec= models.CharField(max_length=255)
    prix= models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    nomp= models.CharField(max_length=255)

    

  
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 # add related name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
class messg(models.Model):
    id=models.AutoField(primary_key=True)
    nome= models.CharField(max_length=200)
    nomc= models.CharField(max_length=200)
    mesg= models.CharField(max_length=200)
class messgm(models.Model):
    id=models.AutoField(primary_key=True)
    nome= models.CharField(max_length=200)
    nomc= models.CharField(max_length=200)
    mesg= models.CharField(max_length=200)
class notp(models.Model):
    id=models.AutoField(primary_key=True)
    nomp= models.CharField(max_length=200)
    notp= models.CharField(max_length=200)
   
class notm(models.Model):
    id=models.AutoField(primary_key=True)
    nomm= models.CharField(max_length=200)
    notm= models.CharField(max_length=200)
    



