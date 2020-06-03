from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
class HomePage(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = "about.html"
    
class TeamView(TemplateView):
    template_name = "team.html"

class MissionView(TemplateView):
    template_name = 'missions.html'

@user_passes_test(lambda u:u.is_superuser)
def send_email(request):
    if request.user.is_superuser:
        subject = request.GET.get('subject')
        message = request.GET.get('message')
        send_mail(subject,message,'indusmegafarms@gmail.com',['abdulsalamfawaz4@gmail.com'])
        return render(request,'send_email.html')