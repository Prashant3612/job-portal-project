from django.urls import path
from .import views
urlpatterns=[
  path('jobs/dashboard',views.dashboard, name="dashboard"),
  path('jobs/create',views.create_job,name='job_create'),
  path('jobs/details/<int:pk>/',views.job_details, name="job_details"),

  path('jobs/applied/<int:pk>',views.applied_jobs ,name='applied_jobs')
]