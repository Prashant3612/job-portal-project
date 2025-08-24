from django.db import models
from django.utils import timezone
from accounts.models import User
from jobs.models import Job


# Create your models here.
STATUS=[('selected','Selected'),
       ('rejected','Rejected')]
class JobApplication(models.Model):
  user=models.ForeignKey('accounts.User',on_delete=models.CASCADE,related_name='applicants')
  job=models.ForeignKey('jobs.Job',on_delete=models.CASCADE,related_name='applied_jobs')
  status=models.CharField(max_length=10,choices=STATUS,default='selected')
  applied_at=models.DateTimeField(default=timezone.now)
