from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
  def create_user(self,email,password=None,user_type=None,**extra_fields):
    if not email:
      raise ValueError('Users must have an email address')
    if not user_type:
      raise ValueError("Users must have a user type")

    email=self.normalize_email(email)
    user=self.model(email=email,user_type=user_type,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,email,password,**extra_fields):
    user=self.create_user(email,password,user_type='ADMIN',**extra_fields)
    user.is_staff=True
    user.is_superuser=True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser,PermissionsMixin):
  USER_TYPE_CHOICES=(('EMPLOYER','Employer'),('CANDIDATE','Candidate'),('ADMIN','Admin'))
  email=models.EmailField(unique=True)
  first_name=models.CharField(max_length=30,blank=True)
  last_name=models.CharField(max_length=30,blank=True)
  user_type=models.CharField(max_length=30,choices=USER_TYPE_CHOICES)
  is_active=models.BooleanField(default=True)
  is_staff=models.BooleanField(default=True)
  objects=UserManager()
  USERNAME_FIELD='email'
  REQUIRED_FIELD=['user_type']

  def _str_(self):
    return self.email


# LOCATION_CHOICES = [
#     ('remote', 'Remote'),
#     ('delhi', 'Delhi'),
#     ('bangalore', 'Bangalore'),
#     ('mumbai', 'Mumbai'),
#     ('hyderabad', 'Hyderabad'),
# ]

# ROLE_CHOICES = [
#     ('frontend', 'Frontend Developer'),
#     ('backend', 'Backend Developer'),
#     ('fullstack', 'Fullstack Developer'),
#     ('data', 'Data Analyst'),
#     ('devops', 'DevOps Engineer'),
# ]

class Role(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Location(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name


class UserProfile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  prof_summary=models.CharField(max_length=300,default="A passionate professional.")
  resume=models.FileField(upload_to='resumes/', null=True, blank=True)
  preferred_roles=models.ManyToManyField(Role,blank=True)
  preferred_location=models.ManyToManyField(Location,blank=True)
  education=models.CharField(max_length=200,default="Not specified")
  skills=models.CharField(max_length=300,default="Not specified")
  phone=models.IntegerField(default=0)
  experience=models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
  current_salary=models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
  linkedin=models.URLField(null=True, blank=True)


  
  


# Create your models here.
