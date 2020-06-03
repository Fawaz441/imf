from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView,View
from .forms import StudentForm,FarmerForm,CompanyForm,SignUpForm,ChallengerForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model,login,authenticate
User = get_user_model()
from django.contrib import messages
from .models import Student,Farmer,Company
from django.shortcuts import redirect
from products.models import Order
# Create your views here.


class UserHome(TemplateView):
    template_name = 'users/user_home.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            current_orders = Order.objects.filter(ordered=True,delivered=False,user=self.request.user)
            context['current_orders'] = current_orders
            return context
        except:
            return context  

# Registering
def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("username")
            last_name = form.cleaned_data.get("last_name")
            category = form.cleaned_data.get("category")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            user = authenticate(username=username,password=password2)
            login(request,user)
            if category == "S":
                return redirect('users:student_reg')
            elif category == "F":
                return redirect('users:farmer_reg')
            elif category == "C":
                return redirect('users:company_reg')
        else:
            messages.error(request,'Error!')
    else:
        form = SignUpForm()
    return render(request,'users/signup.html',{'form':form})

# Choices -- student,farmer and company
def choices(request):
    return render(request,'users/choices.html')

class StudentReg(View):
    def get(self,*args, **kwargs):
        form = StudentForm()
        return render(self.request,'users/student_form.html',{'form':form})
    
    def post(self,*args, **kwargs):
        form = StudentForm(self.request.POST or None)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            student = Student.objects.create(
                phone_number = phone_number,
                location=location,
                user = self.request.user,
            )
            student.save()
            messages.success(self.request,'Successfully registered')
            return redirect('users:user_home')
            
        else:
            messages.warning(self.request,'Form not valid')
            return redirect('users:student_reg')
        

class FarmerReg(View):
    def get(self,*args, **kwargs):
        form = FarmerForm()
        return render(self.request,'users/farmer_form.html',{'form':form})
    
    def post(self,*args, **kwargs):
        form = FarmerForm(self.request.POST or None)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            farm_name = form.cleaned_data.get('farm_name')
            land_size = form.cleaned_data.get('land_size')
            major_products = form.cleaned_data.get('major_products')
            farmer = Farmer.objects.create(
                user = self.request.user,
                land_size = land_size,
                location = location,
                farm_name = farm_name,
                major_products = major_products
            )
            farmer.save()
            messages.success(self.request,'Successfully registered')            
        else:
            messages.warning(self.request,'Form not valid')
        return redirect('users:user_home')


class CompanyReg(View):
    def get(self,*args, **kwargs):
        form = CompanyForm()
        return render(self.request,'users/company_form.html',{'form':form})
    
    def post(self,*args, **kwargs):
        form = CompanyForm(self.request.POST or None)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            company_name = form.cleaned_data.get('company_name')
           
            company = Company.objects.create(
                user = self.request.user,
                phone_number = phone_number,
                location = location,
                company_name = company_name
            )
            company.save()
            messages.success(self.request,'Successfully registered')            
        else:
            messages.warning(self.request,'Form not valid')
        return redirect('users:user_home')


def imchallenge(request):
    form = ChallengerForm()
    if request.method == 'POST':
        form = ChallengerForm(request.POST)
        if form.is_valid():
            messages.success(request,"Email submitted successfully")
            return redirect('users:imchallenge')
        else:
            messages.error(request,'Email not valid')
            return redirect('users:imchallenge')
    else:
        form = ChallengerForm()
    return render(request,'imchallenge.html',{'form':form})
