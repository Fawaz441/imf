from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth.views import LogoutView,LoginView,PasswordResetView,PasswordResetConfirmView,\
PasswordResetDoneView,PasswordResetCompleteView,PasswordChangeView

app_name = 'users'
urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('user_home/', views.UserHome.as_view(), name='user_home'),
    path('choices_reg',views.choices,name='choices'),
    path('reg/student',views.StudentReg.as_view(),name='student_reg'),
    path('reg/farmer',views.FarmerReg.as_view(),name='farmer_reg'),
    path('reg/company',views.CompanyReg.as_view(),name='company_reg'),
    path('imchallenge/',views.imchallenge,name='imchallenge'),
    path('reset_password',PasswordResetView.as_view(subject_template_name='users/subject_template.txt',email_template_name='users/email_template.html',template_name='users/password_reset.html',success_url = 'password_reset_done'),name='password_reset'),
    path('password_reset_done',PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm',PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('change_password',PasswordChangeView.as_view(template_name='users/password_change.html',success_url='login'),name='password_change'),
    ]