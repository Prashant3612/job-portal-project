from django.shortcuts import render,get_object_or_404,redirect
from .forms import SignupForm,UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import User,UserProfile

def signup(request):
  if request.method=='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'accounts/sucess.html')
  else:
    form=SignupForm()
  return render(request,'accounts/signup.html',{'form':form})


@login_required(login_url='/accounts/login/')
def create_profile(request):
  if hasattr(request.user, 'userprofile'):
    # Profile already exists
    return redirect('prof_update')  
  if request.method=='POST':
    form=UserProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user 
      profile.save()
      return redirect(request,'prof_details')
  else:
    form=UserProfileForm()
  return render(request,'accounts/profile_create.html',{'form':form})


@login_required(login_url='/accounts/login/')
def profile_view(request,pk):
  prof=get_object_or_404(UserProfile,pk=pk)
  print(pk,' ',prof)
  return render(request,'accounts/profile_view.html',{'prof':prof})

def prof_update(request,pk):
  prof=get_object_or_404(UserProfile,pk=pk)
  if request.method=='POST':
    form=UserProfileForm(request.POST,instance=prof)
    if form.is_valid():
  
      form.save()
      return redirect('prof_details',pk=pk)
  else:
    form=UserProfileForm(instance=prof)
  return render(request,'accounts/profile_create.html',{'form':form})



# Create your views here.
