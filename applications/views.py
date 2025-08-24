from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from applications.models import JobApplication

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if JobApplication.objects.filter(user=request.user, job=job).exists():
       
        return redirect('job_details', pk=job.pk)

    JobApplication.objects.create(
        user=request.user,
        job=job,
        status='selected'  
    )

    return redirect('job_details', pk=job.pk)

@login_required
def applicatns_views(request):
  applicants=JobApplications.all()
  return render(request,'applications/template/applications/applicants_view.html',{'applicants':applicants})