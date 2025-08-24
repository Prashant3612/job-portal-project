from django.db import models
from django.conf import settings


# Create your models here.
class Job(models.Model):
  title=models.CharField(max_length=200)
  description=models.TextField()
  location=models.CharField(max_length=200)
  company=models.CharField(max_length=100)
  salary=models.DecimalField(max_digits=10, decimal_places=2)
  posted_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  
