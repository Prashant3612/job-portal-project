from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns=[

  
  path('',views.signup,name='signup_form'),
  path('accounts/login',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
  path('accounts/logout',auth_views.LogoutView.as_view(),name='logout'),

  path('accounts/success_logout/', TemplateView.as_view(template_name='accounts/success_logout.html'), name='success_logout'),

  path('accounts/profile/create',views.create_profile, name='create_prof'),
  path('accounts/profile/view/<int:pk>/',views.profile_view, name='prof_details'),
  path('accounts/profile/update/<int:pk>',views.prof_update, name='prof_update')
]