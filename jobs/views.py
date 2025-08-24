from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import JobForm
from .models import Job
from applications.models import JobApplication
from accounts.models import User

# Create your views here.

def create_job(request):
  if request.method=='POST':
    form=JobForm(request.POST)
    if form.is_valid():
      job = form.save(commit=False)
      job.posted_by = request.user
      job.save()
      return redirect('dashboard')
  else:
    form=JobForm()
  return render(request,'jobs/create_job.html',{'form':form})

def dashboard(request):
  if request.user.user_type == 'EMPLOYER':
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})
  elif request.user.user_type == 'CANDIDATE':
    jobs = Job.objects.all()
    return render(request, 'jobs/candidate_dashboard.html', {'jobs': jobs})
  else:
    return HttpResponseForbidden("Unauthorized access.")



def job_details(request,pk):
  job=get_object_or_404(Job,pk=pk)
  print('job_details',job)
  if request.user.user_type=='EMPLOYER':
    
    job_applications = JobApplication.objects.filter(job=job)
    return render(request, 'jobs/job_details.html', {
        'job': job,
        'job_applications': job_applications
    })
  else:
    
    return render(request,'jobs/job_details.html',{'job':job})


def applied_jobs(request,pk):
  user=get_object_or_404(User,pk=pk)
  # user=request.user
  # job=JobApplication.objects.all()
  jobs=JobApplication.objects.filter(user=user)
  # print('jobs',job)
  print(jobs.values())
  return render(request,'jobs/applied_jobs.html',{'jobs':jobs, 'user':user
  })


