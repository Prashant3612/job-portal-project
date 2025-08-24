from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
  class Meta:
    model=User
    fields=['email','first_name','last_name','user_type',]

class UserProfileForm(forms.ModelForm):
  class Meta:
    model=UserProfile
    fields=['prof_summary','resume','preferred_roles','preferred_location','education','skills','phone','experience','current_salary','linkedin']